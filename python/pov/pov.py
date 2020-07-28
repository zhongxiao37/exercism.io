from json import dumps
from collections import namedtuple

Path = namedtuple('Path', 'path')

class Tree(object):
    def __init__(self, label, children=[]):
        self.label = label
        self.children = list(children)

    def __dict__(self):
        return {self.label: [c.__dict__() for c in sorted(self.children)]}

    def __str__(self, indent=None):
        return dumps(self.__dict__(), indent=indent)

    def __lt__(self, other):
        return self.label < other.label

    def __eq__(self, other):
        return self.__dict__() == other.__dict__()

    def from_pov(self, from_node):
        def from_specific_node_to_parent(specific_node, path):
            if len(path) == 0:
                return None
            parent = path.pop()
            new_tree = Tree(parent.label)
            specific_node_in_children = next(child for child in parent.children if child.label == specific_node)
            parent.children.remove(specific_node_in_children)
            new_tree.children = parent.children
            additional_child = from_specific_node_to_parent(new_tree.label, path)
            if additional_child is not None:
                # new_tree.children += [additional_child]
                new_tree.children.append(additional_child)
            return new_tree

        path = self.find_the_path_to_specific_node(from_node)

        tree_from_pov = path.pop()
        new_child = from_specific_node_to_parent(tree_from_pov.label, path)
        if new_child is not None:
            tree_from_pov.children.append(new_child)
        
        return tree_from_pov

    def path_to(self, from_node, to_node):
        new_tree = self.from_pov(from_node)
        path = new_tree.find_the_path_to_specific_node(to_node)
        return [n.label for n in path]

    def find_the_path_to_specific_node(self, specific_node):
        paths = []
        paths.append([self])
        for pth in paths:
            while True:
                if pth[-1].label == specific_node:
                    break
                if len(pth[-1].children) == 0:
                    break
                elif len(pth[-1].children) > 1:
                    for child in pth[-1].children[1:]:
                        new_path = pth.copy()
                        new_path.append(child)
                        paths.append(new_path)
                
                pth.append(pth[-1].children[0])
        
        try:
            path = next(pth for pth in paths if pth[-1].label == specific_node)
        except StopIteration:
            raise ValueError('node does not exist')
        
        return path
