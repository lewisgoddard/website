#!/usr/bin/env python3
# Generator for _data/cpu-scores.yml.
# Reads static specs (_data/cpus.yml) and raw price data (cpu_prices.yml)
# and emits one map keyed by full CPU name, containing price + use-case scores.
#
# scores: raw use-case performance scores (not price adjusted)
#   gaming     - weighted blend of cache/single/pcie/multi + iGPU bonus
#   general    - weighted blend of single + multi; null if no iGPU
#   workbench  - raw multi-core perf
# values: 0..100, normalised perf-per-£ for the same keys in scores
#   gaming/general/workbench are null when price is unknown
#
# Single- and multi-core perf use passmark_single / passmark_multi from cpus.yml
# when present, falling back to turbo clock proxies for chips not yet measured.

import yaml
from pathlib import Path

HERE = Path(__file__).resolve().parent
CPUS_FILE = HERE.parent.parent / '_data' / 'cpus.yml'
RAW_PRICES_FILE = HERE / 'cpu_prices.yml'
OUT_FILE = HERE.parent.parent / '_data' / 'cpu-scores.yml'

WEIGHTS_GAMING = {
    'cache':       0.20,
    'single':      0.20,
    'pcie':        0.20,
    'multi_bonus': 0.30,
    'igpu_bonus':  0.10,
}
WEIGHTS_GENERAL = {
    'cache':  0.25,
    'single': 0.50,
    'multi':  0.50,
}
WEIGHTS_WORKBENCH = {
    'cache':  0.10,
    'single': 0.10,
    'multi':  0.80,
    'pcie':   0.20,
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


def pcie_gen_for(socket, gen, name):
    # Desktop CPU-side PCIe generation used for scoring.
    if name == 'AMD Ryzen 5 8500G':
        return 3
    if socket == 'AM4':
        if str(gen) == '4000':
            return 3
        if name in {'AMD Ryzen 5 5500', 'AMD Ryzen 5 5600G', 'AMD Ryzen 7 5700G'}:
            return 3
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


def norm_cache_mb(values):
    # Piecewise cache scale: 16 MB -> 0.0, 32 MB -> 0.5, 96 MB -> 1.0.
    out = []
    for v in values:
        if v is None:
            out.append(None)
        else:
            cache_mb = float(v)
            if cache_mb <= 16.0:
                out.append(0.0)
            elif cache_mb <= 32.0:
                out.append((cache_mb - 16.0) / 16.0 * 0.5)
            elif cache_mb <= 96.0:
                out.append(0.5 + ((cache_mb - 32.0) / 64.0 * 0.5))
            else:
                out.append(1.0)
    return out


def norm_pcie_gen(values):
    # Fixed PCIe scale requested by user: Gen3=0.0, Gen4=0.8, Gen5=1.0.
    mapping = {3: 0.0, 4: 0.8, 5: 1.0}
    out = []
    for v in values:
        if v is None:
            out.append(None)
        else:
            out.append(mapping.get(int(v), 0.0))
    return out


def scale_pct(values):
    return [round(v * 100) if v is not None else None for v in values]


def main():
    cpus = load_yaml(CPUS_FILE)
    raw = load_yaml(RAW_PRICES_FILE)

    rows = []
    for socket, gen, name, spec in iter_cpus(cpus):
        derived = {
            'pcie_gen': pcie_gen_for(socket, gen, name),
            'has_igpu': bool(spec.get('gpu')),
            'total_cores': parse_cores(spec.get('cores') or 0),
            'single_perf': spec.get('passmark_single'),
            'multi_perf':  spec.get('passmark_multi'),
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
    n_cache  = norm_cache_mb([r['cache']                  for r in rows])
    n_single = norm([r['derived']['single_perf'] for r in rows])
    n_multi  = norm([r['derived']['multi_perf']  for r in rows])
    n_pcie   = norm_pcie_gen([r['derived']['pcie_gen']    for r in rows])
    igpu     = [1 if r['derived']['has_igpu'] else 0 for r in rows]

    gaming_perf = []
    general_perf = []
    workbench_perf = []
    for i, r in enumerate(rows):
        if r['derived']['pcie_gen'] <= 3:
            gaming_perf.append(None)
        else:
            gaming_perf.append(
                WEIGHTS_GAMING['cache']       * (n_cache[i]  or 0)
              + WEIGHTS_GAMING['single']      * (n_single[i] or 0)
              + WEIGHTS_GAMING['pcie']        * (n_pcie[i]   or 0)
              + WEIGHTS_GAMING['multi_bonus'] * (n_multi[i]  or 0)
              + WEIGHTS_GAMING['igpu_bonus']  * igpu[i]
            )
        general_perf.append(
            WEIGHTS_GENERAL['cache']  * (n_cache[i]  or 0)
          + WEIGHTS_GENERAL['single'] * (n_single[i] or 0)
          + WEIGHTS_GENERAL['multi']  * (n_multi[i]  or 0)
            if r['derived']['has_igpu'] else None
        )
        workbench_perf.append(
            WEIGHTS_WORKBENCH['cache']    * (n_cache[i]  or 0)
            + WEIGHTS_WORKBENCH['single'] * (n_single[i] or 0)
            + WEIGHTS_WORKBENCH['multi']  * (n_multi[i]  or 0)
        )

    # Value is perf-per-pound. No price -> no value.
    def per_pound(perf_values):
        out = []
        for i, perf in enumerate(perf_values):
            price = rows[i]['price']
            if perf is None or not price or price <= 0:
                out.append(None)
            else:
                out.append(perf / price)
        return out

    gaming_value_raw    = per_pound(gaming_perf)
    general_value_raw   = per_pound(general_perf)
    workbench_value_raw = per_pound(workbench_perf)

    gaming_value_pct    = scale_pct(norm(gaming_value_raw))
    general_value_pct   = scale_pct(norm(general_value_raw))
    workbench_value_pct = scale_pct(norm(workbench_value_raw))

    gaming_score_pct    = scale_pct(norm(gaming_perf))
    general_score_pct   = scale_pct(norm(general_perf))
    workbench_score_pct = scale_pct(norm(workbench_perf))
    priced = sum(1 for r in rows if r['price'])

    out = {}
    for i, r in enumerate(rows):
        out[r['name']] = {
            'price': ({'min': r['price'], 'offers': r['offers'], 'updated': r['updated']}
                      if r['price'] is not None else None),
            'derived': r['derived'],
            'scores': {
                'gaming':    round(gaming_score_pct[i], 6) if gaming_perf[i] is not None else None,
                'general':   round(general_score_pct[i], 6) if general_perf[i] is not None else None,
                'workbench': round(workbench_score_pct[i], 6) if workbench_perf[i] is not None else None,
            },
            'value': {
                'gaming':    gaming_value_pct[i],
                'general':   general_value_pct[i],
                'workbench': workbench_value_pct[i],
            },
        }

    save_yaml(out, OUT_FILE)
    print(f'Wrote {len(out)} entries to {OUT_FILE.relative_to(HERE.parent.parent)} ({priced} with prices/values)')


if __name__ == '__main__':
    main()
