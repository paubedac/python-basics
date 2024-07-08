class Deque:
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def is_empty(self):
        return self.items == []

    def add_right(self, item):
        self.items.append(item)

    def add_left(self, item):
        self.items.insert(0, item)

    def remove_right(self):
        if self.size() > 0:
            return self.items.pop()
        return ("No element in the deque to be removed")

    def remove_left(self):
        if self.size() > 0:
            return self.items.pop(0)
        return ("No element in the deque to be removed")