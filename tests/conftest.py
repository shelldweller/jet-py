import json
import os

import pytest

class TestWriter():
    def __init__(self):
        self.buffer = []

    def write(self, record: dict):
        self.buffer.append(record)

    def close(self):
        pass


def _load_json_fixture(relative_path):
    path = os.path.join(
        os.path.dirname(__file__),
        'data',
        relative_path
    )
    with open(path) as f:
        return json.load(f)


@pytest.fixture
def oliver_sacks_books():
    return _load_json_fixture('oliver-sacks-books.json')


@pytest.fixture
def country_aruba():
    return _load_json_fixture('aruba.json')


@pytest.fixture
def country_aruba_reader():
    yield _load_json_fixture('aruba.json')


@pytest.fixture
def test_writer():
    return TestWriter()
