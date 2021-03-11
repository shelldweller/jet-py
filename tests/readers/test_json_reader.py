import io

from jet.readers import json_reader


def test_json_reader():
    files = [
        io.StringIO('''
            {"doc": 1}
        '''),
        io.StringIO('''
            [
                {"doc": 2},
                {"doc": 3}
            ]
        ''')
    ]
    docs = list(json_reader(files))
    assert docs == [
        {'doc': 1},
        {'doc': 2},
        {'doc': 3},
    ]
