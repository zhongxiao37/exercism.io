import re

class SgfTree(object):
    def __init__(self, properties=None, children=None):
        self.properties = properties or {}
        self.children = children or []

    def __eq__(self, other):
        if not isinstance(other, SgfTree):
            return False
        for k, v in self.properties.items():
            if k not in other.properties:
                return False
            if other.properties[k] != v:
                return False
        for k in other.properties.keys():
            if k not in self.properties:
                return False
        if len(self.children) != len(other.children):
            return False
        for a, b in zip(self.children, other.children):
            if a != b:
                return False
        return True

    def __ne__(self, other):
        return not self == other


def parse(input_string):
    if len(input_string) < 3:
        raise ValueError('Input string length should be larger than 2')
    
    node = parse_nodes(input_string[1:-1])
    return node

def parse_nodes(input_string):
    parent, children = split_string(input_string)
    parent = parse_single_node(parent)
    for child in children:
        parent.children.append(parse_nodes(child))
    return parent

# return parent and children for ()() case
def split_string(input_string):
    if '(' in input_string:
        separator_index = min([i for i, e in enumerate(input_string) if e == '('])
    else:
        return input_string, []
    
    parent = input_string[:separator_index]    
    
    if ')(' in input_string[separator_index:]:
        children = [re.sub(r'\(|\)', '', x) for x in str.split(input_string[separator_index:], ')(')]
    else:
        children = [input_string[separator_index:]]
    
    return parent, children

# parse normal node without ()() case
def parse_single_node(string):
    if string[0] == ';':
        string = string[1:]
    if ';' in string:
        separator_index = min([i for i, e in enumerate(string) if e == ';'])
        parent = parse_property(string[:separator_index])
        parent.children = [parse_single_node(string[separator_index:])]
    else:
        parent = parse_property(string)
    
    return parent


def parse_property(string):
    if len(string) == 0:
        return SgfTree()

    nodes = re.findall(r"([A-Za-z]+)((?:\[(?:(?<=\\)\[|[^[])*\])+)", string)
    if len(nodes) == 0:
        raise ValueError('Regex parsing error' + string)
    properties = {}
    for node in nodes:
        if any(x.islower() for x in list(node[0])):
            raise ValueError('Key should not be lower case')
        values = re.findall(r'\[(?:(?<=\\)\[|[^[])*\]', node[1])
        values = [re.sub(r'\t', ' ', x[1:-1]) for x in values]
        values = [re.sub(r'\\', '', x) for x in values]
        properties[node[0]] = values
    
    return SgfTree(properties)