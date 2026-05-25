#!/usr/bin/env python3
# Poll the Idealo job ids in cpu_jobs.yml. Successful results are written to
# cpu_prices.yml (keyed by Idealo id). Successful jobs are removed from
# cpu_jobs.yml. Run cpu_score.py afterwards to produce _data/cpu-scores.yml.

import os
import sys
import json
import yaml
import requests
from pathlib import Path

HERE = Path(__file__).resolve().parent
JOBS_FILE = HERE / 'cpu_jobs.yml'
RAW_PRICES_FILE = HERE / 'cpu_prices.yml'

API_BASE = 'https://price-analytics.p.rapidapi.com/poll-job/'
RAPIDAPI_HOST = 'price-analytics.p.rapidapi.com'
RESULT_FIELDS = ['price_min', 'offers_count', 'offers']


def load_yaml(path):
    if not path.exists():
        return {}
    with open(path) as f:
        return yaml.safe_load(f) or {}


def save_yaml(data, path):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, 'w') as f:
        yaml.dump(data, f, indent=2, sort_keys=False)


def main():
    api_key = os.environ.get('RAPIDAPI_KEY')
    if not api_key:
        sys.exit('RAPIDAPI_KEY environment variable is not set.')

    headers = {'x-rapidapi-key': api_key, 'x-rapidapi-host': RAPIDAPI_HOST}

    jobs = load_yaml(JOBS_FILE)
    prices = load_yaml(RAW_PRICES_FILE)
    if not jobs:
        print('No pending jobs.')
        return

    finished = pending = failed = 0
    done_ids = []
    prices_changed = False

    for cpu_id, job_id in list(jobs.items()):
        if not job_id:
            continue

        try:
            resp = requests.get(f'{API_BASE}{job_id}', headers=headers, timeout=30)
            resp.raise_for_status()
            status = resp.json()
        except (requests.RequestException, json.JSONDecodeError) as e:
            print(f'  ERROR polling job {job_id} (cpu {cpu_id}): {e}')
            failed += 1
            continue

        state = status.get('status')
        if state == 'pending':
            pending += 1
            continue
        if state != 'finished':
            failed += 1
            print(f'  job {job_id} state={state!r}')
            continue

        results = status.get('results') or []
        if not (results and isinstance(results[0], dict) and results[0].get('success')):
            failed += 1
            print(f'  job {job_id} returned no usable result')
            continue

        content = results[0].get('content') or {}
        if str(content.get('id')) != cpu_id:
            failed += 1
            print(f'  job {job_id}: id mismatch (expected {cpu_id}, got {content.get("id")})')
            continue

        entry = {k: content.get(k) for k in RESULT_FIELDS}
        entry['updated_at'] = results[0].get('updated_at')
        prices[cpu_id] = entry
        prices_changed = True
        done_ids.append(cpu_id)
        finished += 1
        print(f'  finished {cpu_id}: £{entry.get("price_min")} ({entry.get("offers_count")} offers)')

    print(f'\nFinished: {finished}  Pending: {pending}  Failed: {failed}')

    if prices_changed:
        save_yaml(prices, RAW_PRICES_FILE)
    if done_ids:
        for cid in done_ids:
            jobs.pop(cid, None)
        save_yaml(jobs, JOBS_FILE)


if __name__ == '__main__':
    main()
