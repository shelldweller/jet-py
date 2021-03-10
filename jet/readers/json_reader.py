import json
from io import TextIOWrapper
from typing import Generator, List


def json_reader(files: List[TextIOWrapper]) -> Generator[dict, None, None]:
    for f in files:
        items = json.load(f)
        if not isinstance(items, list):
            items = [items]
        for item in items:
            yield item
