class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []
        self.oldest = 0

    def append(self, item):
        if len(self.storage) < self.capacity:
            self.storage.append(item)
        else:
            self.storage[self.oldest] = item
            if self.oldest == self.capacity - 1:
                self.oldest = 0
            else:
                self.oldest += 1   

    def get(self):
        return self.storage