import io

from jet.readers import jsonl_reader


def test_jsonl_reader(capsys):
    files = [
        io.StringIO('''invalid\n{"doc": 1}\n{"doc": 2}''')
    ]
    docs = list(jsonl_reader(files))
    captured = capsys.readouterr()
    assert docs == [
        {'doc': 1},
        {'doc': 2},
    ]
    assert captured.err == "ERROR: invalid json in 'invalid\\n'\n"
