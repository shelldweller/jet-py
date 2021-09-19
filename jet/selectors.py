from typing import Any, Generator, Tuple

from .json_path import JsonPath


DEFAULT_SELECTOR = lambda x:x


class JsonPathSelector():
    def __init__(self, select_expressions: str):
        self.selectors = [JsonPath(x) for x in select_expressions.strip().split()]

    def __call__(self, doc: dict) -> Generator[Tuple[str,Any], None, None]:
        for selector in self.selectors:
            yield [ (selector.path, result) for result in selector.resolve(doc) ]
