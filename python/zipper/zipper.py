class Zipper(object):
    @staticmethod
    def from_tree(tree):
        return Zipper(tree)

    def __init__(self, tree):
        self.tree = tree
        self.tree_ptr = tree
        self.parents = []

    def value(self):
        return self.tree_ptr['value']

    def set_value(self, value):
        self.tree_ptr['value'] = value
        return self

    def left(self):
        self.parents.append(self.tree_ptr)
        if self.tree_ptr['left'] is None:
            return None
        else:
            self.tree_ptr = self.tree_ptr['left']
            return self

    def set_left(self, left):
        self.tree_ptr['left'] = left
        return self

    def right(self):
        self.parents.append(self.tree_ptr)
        if self.tree_ptr['right'] is None:
            return None
        else:
            self.tree_ptr = self.tree_ptr['right']
            return self

    def set_right(self, right):
        self.tree_ptr['right'] = right
        return self

    def up(self):
        if len(self.parents) == 0:
            return None
        self.tree_ptr = self.parents.pop()
        return self

    def to_tree(self):
        self.tree_ptr = self.tree
        self.parents = []
        return self.tree
