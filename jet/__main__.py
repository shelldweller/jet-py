#!/usr/bin/env python

import argparse

from .main import main
from .readers import json_reader
from .writers import CsvWriter, JsonLineWriter

OUTPUT_FORMATS = {
    'jsonl': JsonLineWriter,
    'csv': CsvWriter,
}


def run_cli():
    parser = argparse.ArgumentParser(description='jet - JSON Extraction Tool')
    parser.add_argument(
        '-s',
        '--select',
        help='space separated JSONPath expressions, e.g., `user.name preferences.color`'
    )

    parser.add_argument(
        '-f',
        '--output-format',
        choices=OUTPUT_FORMATS.keys(),
        default='jsonl'
    )
    parser.add_argument(
        'files',
        nargs='+',
        type=argparse.FileType('r'),
        help='Files to read from'
    )
    args = parser.parse_args()

    main(
        args.select,
        json_reader(args.files),
        OUTPUT_FORMATS[args.output_format]() # TODO: output file name
    )

if __name__ == '__main__':
    print('wat?')
    run_cli()
