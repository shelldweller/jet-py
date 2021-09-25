from typing import Any, Dict, Generator

from .json_path import JsonPath

DEFAULT_SELECTOR = lambda x:x


class JsonPathSelector():
    def __init__(self, select_expressions: str):
        self.selectors = [JsonPath(x) for x in select_expressions.strip().split()]

    def __call__(self, doc: dict) -> Generator[Dict[str,Any], None, None]:
        return { x.path:x.resolve(doc) for x in self.selectors }
