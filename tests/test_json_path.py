import pytest
from jet.json_path import JsonPath, JsonPathError


def test_shallow_path(country_aruba):
    value = JsonPath('name').resolve(country_aruba)
    assert list(value) == [country_aruba['name']]


def test_nested_path(country_aruba):
    value = JsonPath('region.value').resolve(country_aruba)
    assert list(value) == [country_aruba['region']['value']]


def test_invalid_path(country_aruba):
    value = JsonPath('none.such').resolve(country_aruba)
    assert list(value) == [None]


def test_invalid_path_with_default(country_aruba):
    value = JsonPath('none.such').resolve(country_aruba, 'Nonesuch')
    assert list(value) == ['Nonesuch']


def test_array_index(oliver_sacks_books):
    actual = JsonPath('items[0].volumeInfo.title').resolve(oliver_sacks_books)
    expected = oliver_sacks_books['items'][0]['volumeInfo']['title']
    assert list(actual) == [expected]


def test_invalid_array_index(oliver_sacks_books):
    value = JsonPath('items[1000].volumeInfo.title').resolve(oliver_sacks_books)
    assert list(value) == [None]


def test_array_star(oliver_sacks_books):
    expected = [x['volumeInfo']['title'] for x in oliver_sacks_books['items']]
    actual = list(JsonPath('items[*].volumeInfo.title').resolve(oliver_sacks_books))
    assert actual == expected


@pytest.mark.parametrize(
    'expression',
    [
        'items[].foo',
        'items].foo',
        'items[',
        'items[[0]]',
    ]
)
def test_jsonpath_syntax_error(expression):
    with pytest.raises(JsonPathError):
        JsonPath(expression)
