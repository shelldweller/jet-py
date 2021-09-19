from typing import Any, Dict, Generator

from .json_path import JsonPath

DEFAULT_SELECTOR = lambda x:x


class JsonPathSelector():
    def __init__(self, select_expressions: str):
        self.selectors = [JsonPath(x) for x in select_expressions.strip().split()]

    def __call__(self, doc: dict) -> Generator[Dict[str,Any], None, None]:
        results = []
        max_len = 0

        # Buffer results. We end up with something like this ("sNrM" means result M for selector N):
        # [ s1r1 s1r2 s1r3 ... ]
        # [ s2r1 s2r2 s2r3 ... ]
        # [ s3r1 ]
        for selector in self.selectors:
            result = list(selector.resolve(doc))
            if len(result) > max_len:
                max_len = len(result)
            results.append(result)

        # And we are transposing them to something like:
        # { s1:s1r1, s2:s2r1, s3:s3r1 }
        # { s1:s1r2, s2:s2r2, s3:s3r1 }
        # { s1:s1r3, s2:s2r3, s3:s3r1 }
        for result_index in range(max_len):
            row = {}
            for selector_index in range(len(self.selectors)):
                if result_index < len(results[selector_index]):
                    result = results[selector_index][result_index]
                else:
                    result = results[selector_index][0]
                row[self.selectors[selector_index].path] = result
            yield row
