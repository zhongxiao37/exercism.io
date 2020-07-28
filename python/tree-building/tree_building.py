class Record():
    def __init__(self, record_id, parent_id):
        self.record_id = record_id
        self.parent_id = parent_id


class Node():
    def __init__(self, record):
        self.record = record
        self.node_id = record.record_id
        self.children = []


def BuildTree(records):
    records.sort(key=lambda x: x.record_id)
    if len(records) == 0:
        return None
    if records[0].record_id != records[0].parent_id:
        raise ValueError('root node should have parent_id 0')
    
    if records[0].record_id != 0 or (records[-1].record_id + 1) != len(records):
        raise ValueError('numbers should be continuous')
    
    if any(r.record_id <= r.parent_id for r in records[1:]):
        raise ValueError('Non-root records should have parent_id pointed to itself')
    
    nodes = [Node(r) for r in records]
    for node in nodes[1:]:
        parent = list(filter(lambda n: n.node_id == node.record.parent_id, nodes))
        if parent:
            parent[0].children.append(node)
        else:
            raise ValueError('parent is missing')
    
    return nodes[0]


    

