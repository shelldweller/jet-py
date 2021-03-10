from typing import Generator

from .json_path import JsonPath
from .writers import BaseWriter


def main(select_expressions: str, reader: Generator[dict, None, None], writer: BaseWriter):
    extractors = [JsonPath(x) for x in select_expressions.strip().split()]
    for item in reader:
        data = { x.path:x.resolve(item) for x in extractors }
        writer.write(data)
