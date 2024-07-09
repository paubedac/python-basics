class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
    
    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
            else:
                self.data = data
    
    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print( self.data),
        if self.right:
            self.right.print_tree()
    
    def find_value(self, search_value):
        if search_value < self.data:
            if self.left is None:
                return str(search_value) + " was not found"
            return self.left.find_value(search_value)
        else if search_value > self.data:
            if self.right is None:
                return str(search_value) + " was not found"
            return self.right.find_value(search_value)
        else:
            print(str(self.data) + " was found")
    
    def depth(self):
        return max(self.left.depth() if self.left else 0, self.right.depth() if self.right else 0) + 1