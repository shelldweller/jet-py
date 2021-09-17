import sys


class BaseWriter:
    def __init__(self, out=None):
        if not out:
            out = sys.stdout
        self.out = out

    def write(self, record: dict):
        ''' Writes the record to stream. '''
        pass

    def close(self):
        '''
        Flush write buffer if applicable and close stream.
        To be called after all records have been written.
        '''
        self.out.close()
