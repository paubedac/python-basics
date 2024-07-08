class Queue:
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def is_empty(self):
        return self.items == []

    def add(self, item):
        self.items.insert(0, item)

    def remove(self):
        if len(self.queue_list) > 0:
            return self.items.pop()
        return ("No element in the queue to be removed")