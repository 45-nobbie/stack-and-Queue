class Q:
    def __init__(self):
        self.item = []
    def is_empty(self):
        return self.item == []
    def enqueue(self, other):
        self.item.insert(0, other)
    def dequeue(self):
        return self.item.pop()
    def size(self):
        return len(self.item)