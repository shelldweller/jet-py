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
            fields.append(int(buffer))
            buffer = ''
            in_bracket = False

        else:
            buffer += char

        if flush and buffer:
            fields.append(buffer)
            buffer = ''

        position += 1

    if buffer:
        fields.append(buffer)

    return fields



class JsonPath:
    def __init__(self, path: str):
        self.path = path
        self._fields = _parse(path)

    def resolve(self, record:dict, default=None):
        result = record
        for field in self._fields:
            if isinstance(result, dict) and field in result:
                result = result[field]
            elif isinstance(result, list) and field < len(result):
                result = result[field]
            else:
                return default
        return result
