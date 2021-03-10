from jet.json_path import JsonPath


def test_shallow_path(country_aruba):
    JsonPath('name').resolve(country_aruba) == country_aruba['name']


def test_nested_path(country_aruba):
    JsonPath('region.value').resolve(country_aruba) == country_aruba['region']['value']


def test_invalid_path(country_aruba):
    JsonPath('none.such').resolve(country_aruba) == None


def test_invalid_path_with_default(country_aruba):
    JsonPath('none.such').resolve(country_aruba, 'Nonesuch') == 'Nonesuch'
