class Value:
    def __init__(self, number : float, prev=set(), op='') -> None:
        self.number = number
        self.prev = prev
        self.op = op
        
    def __repr__(self) -> str:
        return f'Value(data={self.number})'
    
    def __add__(self, other):
        value = Value(self.number + other.number, set([self, other]), '+')
        return value    
    
    def __mul__(self, other):
        value = Value(self.number * other.number, set([self, other]), '*')
        return value
    

def trace_rec(node : Value, nodes : set, edges : set) -> tuple[set, set]:
    nodes.add(node)
    
    if len(node.prev) == 0:
        return nodes, edges
    
    res_nodes = set([node])
    res_edges = set()
    nodes.add(node)
    
    for element in node.prev:
        edges.add((node, element))
        rec_nodes, rec_edges = trace_rec(element, nodes, edges)
        
        res_nodes = res_nodes | rec_nodes
        res_edges = res_edges | rec_edges
        
    return res_nodes, res_edges
    
    
def trace(node: Value) -> tuple[set, set]:
    return trace_rec(node, set(), set())


def main() -> None:
    x = Value(2.0)
    y = Value(-3.0)
    z = Value(10.0)
    result = x * y + z

    nodes, edges = trace(result)
    print(f'{nodes=}')
    print(f'{edges=}')

main()