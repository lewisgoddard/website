#!/usr/bin/env python3
# Generator for _data/cpu-scores.yml.
# Reads static specs (_data/cpus.yml) and raw price data (cpu_prices.yml)
# and emits one map keyed by full CPU name, containing price + use-case scores.
#
# Use-case scores (0..100, normalised across the priced pool).
# Every score is per-£ — all three are null when price is unknown.
#   gaming     - (cache + single + pcie + multi/igpu bonus) / price
#   general    - (single + multi) / price; null if no iGPU (hard requirement)
#   workbench  - multi-core perf / price
#
# Single- and multi-core perf are currently proxied by turbo clock and
# turbo * total_cores. Swap for real benchmark data when available.

import yaml
from pathlib import Path

HERE = Path(__file__).resolve().parent
CPUS_FILE = HERE.parent.parent / '_data' / 'cpus.yml'
RAW_PRICES_FILE = HERE / 'cpu_prices.yml'
OUT_FILE = HERE.parent.parent / '_data' / 'cpu-scores.yml'

WEIGHTS_GAMING = {
    'cache':       0.40,
    'single':      0.35,
    'pcie':        0.10,
    'multi_bonus': 0.05,
    'igpu_bonus':  0.10,
}
WEIGHTS_GENERAL = {
    'single': 0.50,
    'multi':  0.50,
}


def load_yaml(path):
    if not path.exists():
        return {}
    with open(path) as f:
        return yaml.safe_load(f) or {}


def save_yaml(data, path):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, 'w') as f:
        yaml.dump(data, f, indent=2, sort_keys=False, default_flow_style=False)


def parse_cores(value):
    if isinstance(value, int):
        return value
    if isinstance(value, str) and '+' in value:
        return sum(int(x) for x in value.split('+'))
    return int(value)


def pcie_gen_for(socket, gen):
    # AM4 platform = PCIe 4. AM5 8000-series APUs = PCIe 4. Everything else = 5.
    if socket == 'AM4':
        return 4
    if socket == 'AM5' and str(gen) == '8000':
        return 4
    return 5


def iter_cpus(cpus):
    for socket, sock in (cpus.get('sockets') or {}).items():
        for gen, gen_data in (sock.get('generations') or {}).items():
            for name, spec in (gen_data or {}).items():
                yield socket, str(gen), name, spec


def norm(values):
    nums = [v for v in values if v is not None]
    if not nums:
        return [None] * len(values)
    hi = max(nums)
    if hi <= 0:
        return [None] * len(values)
    return [(v / hi if v is not None else None) for v in values]


def scale_pct(values):
    return [round(v * 100) if v is not None else None for v in values]


def main():
    cpus = load_yaml(CPUS_FILE)
    raw = load_yaml(RAW_PRICES_FILE)

    rows = []
    for socket, gen, name, spec in iter_cpus(cpus):
        turbo = float(spec.get('turbo') or 0)
        total_cores = parse_cores(spec.get('cores') or 0)
        derived = {
            'pcie_gen': pcie_gen_for(socket, gen),
            'has_igpu': bool(spec.get('gpu')),
            'total_cores': total_cores,
            'single_perf': turbo,
            'multi_perf': round(total_cores * turbo, 2),
        }
        cpu_id = str(spec.get('id') or '') or None
        rr = raw.get(cpu_id) if cpu_id else None
        rr = rr if isinstance(rr, dict) else {}
        rows.append({
            'name':    name,
            'cache':   spec.get('cache') or 0,
            'derived': derived,
            'price':   rr.get('price_min'),
            'offers':  rr.get('offers_count'),
            'updated': rr.get('updated_at'),
        })

    # Component-wise normalisation, then weighted sum, then final normalisation.
    n_cache  = norm([r['cache']                  for r in rows])
    n_single = norm([r['derived']['single_perf'] for r in rows])
    n_multi  = norm([r['derived']['multi_perf']  for r in rows])
    n_pcie   = norm([r['derived']['pcie_gen']    for r in rows])
    igpu     = [1 if r['derived']['has_igpu'] else 0 for r in rows]

    gaming_perf = []
    general_perf = []
    workbench_perf = []
    for i, r in enumerate(rows):
        gaming_perf.append(
            WEIGHTS_GAMING['cache']       * (n_cache[i]  or 0)
          + WEIGHTS_GAMING['single']      * (n_single[i] or 0)
          + WEIGHTS_GAMING['pcie']        * (n_pcie[i]   or 0)
          + WEIGHTS_GAMING['multi_bonus'] * (n_multi[i]  or 0)
          + WEIGHTS_GAMING['igpu_bonus']  * igpu[i]
        )
        general_perf.append(
            WEIGHTS_GENERAL['single'] * (n_single[i] or 0)
          + WEIGHTS_GENERAL['multi']  * (n_multi[i]  or 0)
            if r['derived']['has_igpu'] else None
        )
        workbench_perf.append(r['derived']['multi_perf'])

    # Every score is perf-per-pound. No price -> no score.
    def per_pound(perf_values):
        out = []
        for i, perf in enumerate(perf_values):
            price = rows[i]['price']
            if perf is None or not price or price <= 0:
                out.append(None)
            else:
                out.append(perf / price)
        return out

    gaming_raw    = per_pound(gaming_perf)
    general_raw   = per_pound(general_perf)
    workbench_raw = per_pound(workbench_perf)

    gaming_pct    = scale_pct(norm(gaming_raw))
    general_pct   = scale_pct(norm(general_raw))
    workbench_pct = scale_pct(norm(workbench_raw))
    priced = sum(1 for r in rows if r['price'])

    out = {}
    for i, r in enumerate(rows):
        out[r['name']] = {
            'price': ({'min': r['price'], 'offers': r['offers'], 'updated': r['updated']}
                      if r['price'] is not None else None),
            'derived': r['derived'],
            'scores': {
                'gaming':    gaming_pct[i],
                'general':   general_pct[i],
                'workbench': workbench_pct[i],
            },
        }

    save_yaml(out, OUT_FILE)
    print(f'Wrote {len(out)} entries to {OUT_FILE.relative_to(HERE.parent.parent)} ({priced} with prices/scores)')


if __name__ == '__main__':
    main()
