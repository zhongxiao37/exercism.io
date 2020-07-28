NODE, EDGE, ATTR = range(3)


class Node(object):
    def __init__(self, name, attrs):
        self.name = name
        self.attrs = attrs

    def __eq__(self, other):
        return self.name == other.name and self.attrs == other.attrs


class Edge(object):
    def __init__(self, src, dst, attrs):
        self.src = src
        self.dst = dst
        self.attrs = attrs

    def __eq__(self, other):
        return (self.src == other.src and
                self.dst == other.dst and
                self.attrs == other.attrs)


class Graph(object):
    def __init__(self, data=None):
        self.nodes = []
        self.edges = []
        self.attrs = {}

        if data is not None:
            if len(data[0]) < 2:
                    raise TypeError('wrong args')
            for klass, *args in data:
                if args is None or len(args) == 0:
                    raise TypeError('missing args')
                if klass == NODE:
                    if len(args) != 2:
                        raise ValueError('wrong params')
                    self.nodes.append(Node(*args))
                elif klass == EDGE:
                    if len(args) != 3:
                        raise ValueError('wrong params')
                    self.edges.append(Edge(*args))
                elif klass == ATTR:
                    if len(args) != 2:
                        raise ValueError('wrong params')
                    self.attrs[args[0]] = args[1]
                else:
                    raise ValueError('unkown class')

            

        
