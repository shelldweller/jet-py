import json
import re

from .exceptions import JetParseException
from .json_path import JsonPath
from .mixins import Resolvable
from typing import Any


OPERATORS = {
    '==': lambda a,b: a == b,
    '=':  lambda a,b: a == b,
    '>=': lambda a,b: a >= b,
    '<=': lambda a,b: a <= b,
    '>':  lambda a,b: a > b,
    '<':  lambda a,b: a < b,
    '!=': lambda a,b: a != b,
    'in': lambda a,b: a in b,
}

DEFAULT_FILTER = lambda _: True


class JsonLiteralResolver(Resolvable):
    def __init__(self, value: str) -> None:
        try:
            self._value = json.loads(value)
        except json.JSONDecodeError as e:
            raise JetParseException(f'Invalid JSON expression {value}') from e

    def resolve(self, *args, **kwargs) -> Any:
        return self._value


def _looks_like_json(value: str) -> bool:
    chars = ('{', '[', '"', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'true', 'false', 'null')
    return next((bool(x) for x in chars if value.startswith(x)), False)


def _load_resolver(value: str) -> Resolvable:
    if _looks_like_json(value):
        return JsonLiteralResolver(value)
    return JsonPath(value)


def _quote_operator(value: str) -> str:
    if re.match(r'^\w+$', value):
        # `in` -> `\bin\b`
        return f'\\b{value}\\b'
    return value


class Filter:
    matcher = re.compile(
        r'\s*(' +
        '|'.join(_quote_operator(x) for x in OPERATORS.keys()) +
        r')\s*'
    )

    def __init__(self, expression: str):
        chunks = self.matcher.split(expression.strip())
        if len(chunks) != 3:
            raise JetParseException(f'Error parsing {expression}')

        self.left = _load_resolver(chunks[0])
        self.operator = OPERATORS[chunks[1]]
        self.right = _load_resolver(chunks[2])

    def __call__(self, record:dict) -> bool:
        return self.operator(self.left.resolve(record), self.right.resolve(record))
