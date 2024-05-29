import graphviz

class Value:
    def __init__(self, number : float, prev=set(), op='', label='') -> None:
        self.number = number
        self.prev = prev
        self.op = op
        self.label = label
        
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


# CODE FROM HERE
def draw_dot(root: Value) -> graphviz.Digraph:
    dot = graphviz.Digraph(filename='01_result', format='svg', graph_attr={
                           'rankdir': 'LR'})  # LR = left to right

    nodes, edges = trace(root)
    for n in nodes:
        uid = str(id(n))
        # for any value in the graph, create a rectangular ('record') node
        dot.node(name=uid, label=f'{{ data: {n.number}}}', shape='record')
        if n.op:
            # if this value is a result of some operation, create an "op" node for the operation
            dot.node(name=uid + n.op, label=n.op)
            # and connect this node to the node of the operation
            dot.edge(uid + n.op, uid)

    for n1, n2 in edges:
        # connect n1 to the "op" node of n2
        dot.edge(str(id(n1)), str(id(n2)) + n2.op)

    return dot
#TO HERE is not mine. It has been provided to me in class by my teacher


def main() -> None:
    a = Value(2.0, label='x')
    b = Value(-3.0, label='y')
    c = Value(10.0, label='z')

    e = a * b
    e.label = 'e'

    d = e + c
    d.label = 'd'
    
    draw_dot(d).render(directory='./graphviz_output', view=True)
    
main()
