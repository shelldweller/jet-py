import json
import os

import pytest


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
    # http://api.worldbank.org/v2/country?format=json&per_page=300
    return {
        "id": "ABW",
        "iso2Code": "AW",
        "name": "Aruba",
        "region": {
            "id": "LCN",
            "iso2code": "ZJ",
            "value": "Latin America & Caribbean"
        },
        "adminregion": {
            "id": "",
            "iso2code": "",
            "value": ""
        },
        "incomeLevel": {
            "id": "HIC",
            "iso2code": "XD",
            "value": "High income"
        },
        "lendingType": {
            "id": "LNX",
            "iso2code": "XX",
            "value": "Not classified"
        },
        "capitalCity": "Oranjestad",
        "longitude": "-70.0167",
        "latitude": "12.5167"
    }
