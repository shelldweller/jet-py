from typing import Generator

from .filters import DEFAULT_FILTER, Filter
from .selectors import DEFAULT_SELECTOR, JsonPathSelector
from .writers import BaseWriter


def main(select_expressions: str, reader: Generator[dict, None, None], writer: BaseWriter, filter_expression: str):
    selector = JsonPathSelector(select_expressions) if select_expressions else DEFAULT_SELECTOR
    doc_filter = Filter(filter_expression) if filter_expression else DEFAULT_FILTER
    for item in filter(doc_filter, reader):
        data = selector(item)
        writer.write(data)
