from typing import List, Dict
from .jobs import read


def get_unique_industries(path: str) -> List[str]:
    data = read(path)
    return list(set(row['industry'] for row in data if row['industry']))


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    return [row for row in jobs if row['industry'] == industry]
