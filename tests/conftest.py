import pytest


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
            "value": "Latin America & Caribbean "
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
