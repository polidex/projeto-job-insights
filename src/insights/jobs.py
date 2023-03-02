from functools import lru_cache
from typing import List, Dict
import csv


@lru_cache
def read(path: str) -> List[Dict]:
    with open(path, encoding="utf-8") as file:
        items = csv.DictReader(file)
        return [row for row in items]


def get_unique_job_types(path: str) -> List[str]:
    job_data = read(path)
    return set([row['job_type'] for row in job_data])


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    return [row for row in jobs if row["job_type"] == job_type]
