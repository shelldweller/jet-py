import json
import re

from .exceptions import JetParseException
from .json_path import JsonPath


OPERATORS = {
    '==': lambda a,b: a == b,
    '=':  lambda a,b: a == b,
    '>=': lambda a,b: a >= b,
    '<=': lambda a,b: a <= b,
    '>':  lambda a,b: a > b,
    '<':  lambda a,b: a < b,
    '!=': lambda a,b: a != b,
}

DEFAULT_FILTER = lambda _: True


class Filter:
    matcher = re.compile(r'([.\w]+)\s*(' + '|'.join(OPERATORS.keys()) + r')\s*(.*)')

    def __init__(self, expression: str):
        match = self.matcher.match(expression.strip())
        if not match:
            raise JetParseException(f'Error parsing {expression}')

        self.json_path = JsonPath(match.group(1))
        self.matcher = OPERATORS[match.group(2)]

        try:
            self.value = json.loads(match.group(3))
        except json.JSONDecodeError as e:
            raise JetParseException(f'Invalid expression {match.groups(3)}') from e

    def __call__(self, record:dict) -> bool:
        return self.matcher(self.json_path.resolve(record), self.value)

