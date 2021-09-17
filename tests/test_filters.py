import pytest
from jet.filters import Filter


@pytest.mark.parametrize(
    'expression,expected',
    [
        # =
        ('name = "Aruba"', True),
        ('name = "Nonesuch"', False),
        ('incomeLevel = { "id": "HIC", "iso2code": "XD", "value": "High income"}', True),
        ('incomeLevel = {}', False),
        # !=
        ('name != "Nonesuch"', True),
        ('name != "Aruba"', False),
        # >
        ('region.iso2code > "A"', True),
        ('region.iso2code > "ZZ"', False),
        # <
        ('region.iso2code < "A"', False),
        ('region.iso2code < "ZZ"', True),
        # >=
        ('region.iso2code >= "ZJ"', True),
        ('region.iso2code >= "ZA"', True),
        ('region.iso2code >= "ZZ"', False),
        # <=
        ('region.iso2code <= "ZJ"', True),
        ('region.iso2code <= "ZA"', False),
        ('region.iso2code <= "ZZ"', True),
    ]
)
def test_simple_filter(expression, expected, country_aruba):
    doc_filter = Filter(expression)
    assert doc_filter(country_aruba) == expected

