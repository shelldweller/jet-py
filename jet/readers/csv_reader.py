import csv
from io import TextIOWrapper
from typing import Generator, List


def csv_reader(files: List[TextIOWrapper]) -> Generator[dict, None, None]:
    for f in files:
        reader = csv.DictReader(f)
        for item in reader:
            yield item
