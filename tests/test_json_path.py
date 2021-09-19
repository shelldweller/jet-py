from jet.json_path import JsonPath


def test_shallow_path(country_aruba):
    assert JsonPath('name').resolve(country_aruba) == country_aruba['name']


def test_nested_path(country_aruba):
    assert JsonPath('region.value').resolve(country_aruba) == country_aruba['region']['value']


def test_invalid_path(country_aruba):
    assert JsonPath('none.such').resolve(country_aruba) == None


def test_invalid_path_with_default(country_aruba):
    assert JsonPath('none.such').resolve(country_aruba, 'Nonesuch') == 'Nonesuch'


def test_array_index(oliver_sacks_books):
    assert JsonPath('items[0].volumeInfo.title').resolve(oliver_sacks_books) == oliver_sacks_books['items'][0]['volumeInfo']['title']
