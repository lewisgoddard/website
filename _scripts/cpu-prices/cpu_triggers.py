#!/usr/bin/env python3
# Trigger Idealo price jobs for every CPU in _data/cpus.yml that has an `id`.
# Writes pending job IDs to cpu_jobs.yml. Skips CPUs whose price in
# cpu_prices.yml is younger than MAX_PRICE_AGE_DAYS.

import os
import sys
import json
import yaml
import requests
from datetime import datetime, timedelta, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
CPUS_FILE = HERE.parent.parent / '_data' / 'cpus.yml'
JOBS_FILE = HERE / 'cpu_jobs.yml'
RAW_PRICES_FILE = HERE / 'cpu_prices.yml'

API_URL = 'https://price-analytics.p.rapidapi.com/search-by-id'
RAPIDAPI_HOST = 'price-analytics.p.rapidapi.com'
MAX_PRICE_AGE_DAYS = 7

PAYLOAD_TEMPLATE = {'source': 'idealo', 'country': 'uk', 'values': ''}


def load_yaml(path):
    if not path.exists():
        return {}
    with open(path) as f:
        return yaml.safe_load(f) or {}


def save_yaml(data, path):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, 'w') as f:
        yaml.dump(data, f, indent=2, sort_keys=False)


def iter_cpus(cpus_data):
    for socket, sock in (cpus_data.get('sockets') or {}).items():
        for gen, gen_data in (sock.get('generations') or {}).items():
            for name, spec in (gen_data or {}).items():
                yield socket, gen, name, spec


def is_stale(entry, max_age_days):
    if not isinstance(entry, dict):
        return True
    ts = entry.get('updated_at')
    if not ts:
        return True
    try:
        if ts.endswith('Z'):
            ts = ts[:-1] + '+00:00'
        dt = datetime.fromisoformat(ts)
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)
        return (datetime.now(timezone.utc) - dt) > timedelta(days=max_age_days)
    except Exception:
        return True


def main():
    api_key = os.environ.get('RAPIDAPI_KEY')
    if not api_key:
        sys.exit('RAPIDAPI_KEY environment variable is not set.')

    headers = {
        'x-rapidapi-key': api_key,
        'x-rapidapi-host': RAPIDAPI_HOST,
        'Content-Type': 'application/x-www-form-urlencoded',
    }

    cpus = load_yaml(CPUS_FILE)
    jobs = load_yaml(JOBS_FILE)
    prices = load_yaml(RAW_PRICES_FILE)

    triggered = skipped_pending = skipped_fresh = no_id = 0
    changed = False

    for _socket, _gen, name, spec in iter_cpus(cpus):
        cpu_id = spec.get('id') if isinstance(spec, dict) else None
        if not cpu_id:
            no_id += 1
            continue
        cpu_id = str(cpu_id)

        if jobs.get(cpu_id):
            skipped_pending += 1
            continue

        if not is_stale(prices.get(cpu_id), MAX_PRICE_AGE_DAYS):
            skipped_fresh += 1
            continue

        payload = {**PAYLOAD_TEMPLATE, 'values': cpu_id}
        try:
            resp = requests.post(API_URL, data=payload, headers=headers, timeout=30)
            resp.raise_for_status()
            job_id = resp.json().get('job_id')
        except (requests.RequestException, json.JSONDecodeError) as e:
            print(f'  ERROR triggering {name} ({cpu_id}): {e}')
            continue

        if not job_id:
            print(f'  WARN no job_id for {name} ({cpu_id})')
            continue

        jobs[cpu_id] = job_id
        triggered += 1
        changed = True
        print(f'  triggered {name} -> job {job_id}')

    print(f'\nTriggered: {triggered}  Pending: {skipped_pending}  Fresh: {skipped_fresh}  No id: {no_id}')
    if changed:
        save_yaml(jobs, JOBS_FILE)


if __name__ == '__main__':
    main()
