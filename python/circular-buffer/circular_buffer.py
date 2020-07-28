class BufferFullException(Exception):
    pass


class BufferEmptyException(Exception):
    pass


class CircularBuffer(object):
    def __init__(self, capacity):
        self.lst = [None for i in range(capacity)]
        self.start_index = capacity // 2
        self.end_index = capacity // 2

    def read(self):
        if self.start_index == self.end_index and all(x == None for x in self.lst):
            raise BufferEmptyException('Empty')
        
        data = self.lst[self.start_index]
        self.lst[self.start_index] = None
        self.start_index = (self.start_index + 1) % len(self.lst)
        return data
 

    def write(self, data):
        if self.start_index == self.end_index and all(x != None for x in self.lst):
            raise BufferFullException('Full')
        self.overwrite(data)

    def overwrite(self, data):
        self.lst[self.end_index] = data
        if self.start_index == self.end_index and all(x != None for x in self.lst):
            self.start_index = (self.start_index + 1) % len(self.lst)
        self.end_index = (self.end_index + 1) % len(self.lst)

    def clear(self):
        self.lst = [None for i in range(len(self.lst))]
