class Tree:
    def __init__(self, data, children = []):
        self.data = data
        self.children = children
    def __str__(self):
        return str(self.data)


