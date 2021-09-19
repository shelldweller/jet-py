from typing import Generator

class JsonPathError(ValueError):
    pass


def _parse(expression: str) -> list:
    fields = []
    buffer = ''
    in_bracket = False
    position = 0

    for char in expression:
        flush = False

        if char == '.':
            flush = True

        elif char == '[':
            if in_bracket:
                raise JsonPathError(f'Unexpected "[" in position {position}')
            in_bracket = True
            flush = True

        elif char == ']':
            if not in_bracket:
                raise JsonPathError(f'Unexpected "]" in position {position}')
            if not buffer:
                raise JsonPathError(f'Invalid JSON Path expression in position {position - 1}')
            if buffer == '*':
                flush = True
            else:
                fields.append(int(buffer))
                buffer = ''
            in_bracket = False

        else:
            buffer += char

        if flush and buffer:
            fields.append(buffer)
            buffer = ''

        position += 1

    if in_bracket:
        raise JsonPathError('"[" was not closed')

    if buffer:
        fields.append(buffer)

    return fields



class JsonPath:
    def __init__(self, path: str):
        self.path = path
        self._fields = _parse(path)

    def _resolve(self, record:dict, fields:list, default=None) -> Generator:
        result = record
        for i, field in enumerate(fields):
            if isinstance(result, dict) and field in result:
                result = result[field]
            elif isinstance(result, list) and isinstance(field, int) and field < len(result):
                result = result[field]
            elif isinstance(result, list) and field == '*':
                for x in result:
                    yield from self._resolve(x, fields[i+1:], default)
                return
            else:
                yield default
                return
        yield result

    # TODO: remove the `default` param; with generator [] would be more suitable
    def resolve(self, record:dict, default=None):
        return self._resolve(record, self._fields, default)
