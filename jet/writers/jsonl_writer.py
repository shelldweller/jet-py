import json

from .base_writer import BaseWriter


class JsonLineWriter(BaseWriter):
    def write(self, record: dict):
        json.dump(record, self.out)
        self.out.write('\n')
