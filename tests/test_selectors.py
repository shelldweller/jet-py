import pytest
from jet.selectors import JsonPathSelector


@pytest.mark.parametrize(
    'expression, expected',
    [
        ('name region.value', { 'name': 'Aruba', 'region.value': 'Latin America & Caribbean' }),
        ('name not.there', { 'name': 'Aruba', 'not.there': None }),
    ]
)
def test_jsonpath_selector(expression, expected, country_aruba):
    actual = JsonPathSelector(expression)(country_aruba)
    assert actual == expected
