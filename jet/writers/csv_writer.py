import csv

from .base_writer import BaseWriter


class CsvWriter(BaseWriter):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.writer = None

    def write(self, record: dict):
        if self.writer is None:
            self.writer = csv.DictWriter(self.out, fieldnames=record.keys())
            self.writer.writeheader()
        self.writer.writerow(record)
