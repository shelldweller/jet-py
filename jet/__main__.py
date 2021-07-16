#!/usr/bin/env python

import argparse
import sys

from .main import main
from .readers import csv_reader, json_reader, jsonl_reader
from .writers import CsvWriter, JsonLineWriter, JsonWriter

OUTPUT_FORMATS = {
    'csv': CsvWriter,
    'json': JsonWriter,
    'jsonline': JsonLineWriter,
}

INPUT_FORMATS = {
    'csv': csv_reader,
    'json': json_reader,
    'jsonline': jsonl_reader,
}


def run_cli():
    parser = argparse.ArgumentParser(description='jet - JSON Extraction Tool')
    parser.add_argument(
        '-s',
        '--select',
        help='Space separated JSONPath expressions, e.g., `user.name preferences.color`'
    )

    parser.add_argument(
        '-f',
        '--filter',
        help='Filter expression, e.g., `user.name = "shelldweller"`'
    )

    parser.add_argument(
        '-o',
        '--output-format',
        choices=OUTPUT_FORMATS.keys(),
        default='jsonline',
        help='Output format, defaults to "jsonline"'
    )
    parser.add_argument(
        '-i',
        '--input-format',
        choices=INPUT_FORMATS.keys(),
        default='json',
        help='Input format, defaults to "json"'
    )
    parser.add_argument(
        'files',
        nargs='*',
        type=argparse.FileType('r'),
        default=[sys.stdin],
        help='Files to read from'
    )
    args = parser.parse_args()

    main(
        args.select,
        INPUT_FORMATS[args.input_format](args.files),
        OUTPUT_FORMATS[args.output_format](),
        filter_expression = args.filter
    )

if __name__ == '__main__':
    run_cli()
