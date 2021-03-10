class JsonPath:
    def __init__(self, path: str):
        # only supporting simple object path for now
        self.path = path
        self._fields = path.split('.')

    def resolve(self, record:dict, default=None):
        result = record
        for field in self._fields:
            if isinstance(result, dict) and field in result:
                result = result[field]
            else:
                return default
        return result
