import sys


class BaseWriter:
    def __init__(self, out=None):
        if not out:
            out = sys.stdout
        self.out = out

    def write(self, record: dict):
        pass
