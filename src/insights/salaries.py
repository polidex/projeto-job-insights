from typing import Union, List, Dict
from .jobs import read


def get_max_salary(path: str) -> int:
    data = read(path)
    max_salary = 0
    for row in data:
        if (row['max_salary'].isnumeric()
        and int(row['max_salary']) > max_salary):
            max_salary = int(row['max_salary'])
    return max_salary


def get_min_salary(path: str) -> int:
    data = read(path)
    min_salary = 0
    for row in data:
        if row["min_salary"].isnumeric() and min_salary == 0:
            min_salary = int(row["min_salary"])
        if (row["min_salary"].isnumeric()
           and int(row["min_salary"]) < min_salary):
            min_salary = int(row["min_salary"])
    return min_salary


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    try:
        salary_range = int(salary)
        minSalary = job["min_salary"]
        maxSalary = job["max_salary"]
        if (int(maxSalary) < int(minSalary)):
            raise ValueError
    except KeyError:
        raise ValueError
    except TypeError:
        raise ValueError
    return int(minSalary) <= salary_range <= int(maxSalary)


def filter_by_salary_range(
    jobs: List[dict],
    salary: Union[str, int]
) -> List[Dict]:
    jobs_range = []
    for row in jobs:
        try:
            if matches_salary_range(row, salary):
                jobs_range.append(row)
        except ValueError:
            ValueError
    return jobs_range
