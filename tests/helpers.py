class TestWriter():
    def __init__(self):
        self.buffer = []

    def write(self, record: dict):
        self.buffer.append(record)

    def close(self):
        pass
