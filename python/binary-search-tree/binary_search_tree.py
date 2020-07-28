class TreeNode(object):
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

    def insert(self, data):
        if data <= self.data:
            if self.left is None:
                self.left = self.__class__(data, None, None)
            else:
                self.left.insert(data)
        else:
            if self.right is None:
                self.right = self.__class__(data, None, None)
            else:
                self.right.insert(data)

    def __str__(self):
        fmt = 'TreeNode(data={}, left={}, right={})'
        return fmt.format(self.data, self.left, self.right)


class BinarySearchTree(object):
    def __init__(self, tree_data):
        self._tree_data = tree_data

    def data(self):
        raw_tree_data = self._tree_data[:]
        data = TreeNode(raw_tree_data.pop(0), None, None)
        while len(raw_tree_data) > 0:
            data.insert(raw_tree_data.pop(0))
        return data


    def sorted_data(self):
        return list(sorted(self._tree_data))
