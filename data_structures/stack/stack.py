class Stack:
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)
    
    def add(self, item):
        self.items.append(item)
    
    def peek(self):
	    return self.items[-1]
    
    def remove(self):
        if self.size() > 0:
            return self.items.pop()
        return ("No element in the stack to be removed")