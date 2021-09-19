import pytest
from jet.selectors import JsonPathSelector


@pytest.mark.parametrize(
    'expression, expected',
    [
        ('name region.value', [[('name', 'Aruba'), ('region.value', 'Latin America & Caribbean')]]),
        ('name not.there', [[('name', 'Aruba'), ('not.there', None)]]),
    ]
)
def test_jsonpath_selector(expression, expected, country_aruba):
    actual = list(JsonPathSelector(expression)(country_aruba))
    print(actual)
    print(expected)
    assert actual == expected


# [
#     [
#         ('name', 'Aruba'), ('region.value', 'Latin America & Caribbean')
#     ],
#     [
#         ('name', 'Cuba'), ('region.value', 'Latin America & Caribbean')
#     ]
# ]
