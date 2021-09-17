import json

from .base_writer import BaseWriter


class JsonWriter(BaseWriter):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.buffer = []

    def write(self, record: dict):
        self.buffer.append(record)

    def close(self):
        json.dump(self.buffer, self.out)
        super().close()
