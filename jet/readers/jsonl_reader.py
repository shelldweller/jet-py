import json
import sys
from io import TextIOWrapper
from typing import Generator, List


def jsonl_reader(files: List[TextIOWrapper]) -> Generator[dict, None, None]:
    for f in files:
        for line in f:
            try:
                yield json.loads(line)
            except json.JSONDecodeError:
                sys.stderr.write(f'ERROR: invalid json in {repr(line)}\n')
