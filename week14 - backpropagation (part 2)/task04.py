from __future__ import annotations
import graphviz


class Value:
    def __init__(self, data: float, _children: tuple = (), _op: str = '', label : str = '') -> None:
        self.data : float =  data
        self._prev = set(_children)
        self._op = _op
        self._label = label
        self._grad : float = 0.0
        
    def __repr__(self) -> str:
        return f'Value(data={self.data})'

    def __add__(self, rhs: Value) -> Value:
        return Value(self.data + rhs.data, _children=(self, rhs), _op='+')

    def __mul__(self, rhs: Value) -> Value:
        return Value(self.data * rhs.data, _children=(self, rhs), _op='*')


def trace(root: Value) -> tuple[set[Value], set[tuple[Value, Value]]]:
    # Build a set of all nodes and edges in a graph
    nodes, edges = set(), set()

    def build(v):
        if v not in nodes:
            nodes.add(v)
            for child in v._prev:
                edges.add((child, v))
                build(child)
    build(root)

    return nodes, edges


def draw_dot(root: Value) -> graphviz.Digraph:
    dot = graphviz.Digraph(filename='01_result', format='svg', graph_attr={
                           'rankdir': 'LR'})  # LR = left to right

    nodes, edges = trace(root)
    for n in nodes:
        uid = str(id(n))
        # for any value in the graph, create a rectangular ('record') node
        dot.node(name=uid, label=f'{{ {n._label} | data: {n.data} | grad: {n._grad}}}', shape='record')
        if n._op:
            # if this value is a result of some operation, create an "op" node for the operation
            dot.node(name=uid + n._op, label=n._op)
            # and connect this node to the node of the operation
            dot.edge(uid + n._op, uid)

    for n1, n2 in edges:
        # connect n1 to the "op" node of n2
        dot.edge(str(id(n1)), str(id(n2)) + n2._op)

    return dot

# def manual_der(root:Value):
#     root._grad = 1
#     if len(root._prev) != 0:
#         prev1, prev2 = tuple(root._prev)
#         manual_der_rec(prev1, root, prev2)
#         manual_der_rec(prev2, root, prev1)


# def manual_der_rec(current : Value, parent1 : Value, parent2 : Value) -> float:
#     if current._op == '+':
#         parent1._grad = current._grad
#         parent2._grad = current._grad
    
#     if current._op == '*':
#         parent1._grad = parent2.value * current._grad
#         parent2._grad = parent1.value * current._grad
    
    
# def manual_der(root:Value):
#     root._grad = 1
#     if len(root._prev) != 0:
#         prev1, prev2 = tuple(root._prev)
#         manual_der_rec(root, prev1, prev2)
#         manual_der_rec(root, prev2, prev1)

# def manual_der_rec(parent : Value, current : Value, other_child : Value) -> float:
#     if parent._op == '+':
#         current._grad = parent._grad
#     if parent._op == '*':
        
    
    
#     if len(root._prev) != 0:
#         for prev in root._prev:
#             manual_der(prev)
    
def manual_der():
    h = 0.001
    
    a = Value(2.0, label='x')
    b = Value(-3.0, label='y')
    c = Value(10.0, label='z')
    f = Value(-2.0, label='f')

    e = a * b
    d = e + c
    old_l = d * f

    a = Value(2.0, label='x')
    b = Value(-3.0, label='y')
    c = Value(10.0, label='z')
    f = Value(-2.0, label='f')
    
    b.data += h
    e = a * b
    d = e + c
    new_l = d * f
    
    print((new_l.data - old_l.data) / h)

def main() -> None:
    manual_der()
    a = Value(2.0, label='x')
    b = Value(-3.0, label='y')
    c = Value(10.0, label='z')
    f = Value(-2.0, label='f')

    e = a * b
    e._label = 'e'

    d = e + c
    d._label = 'd'
    
    old_L = d * f
    
    old_L._grad = 1; f._grad = 4; d._grad = -2; e._grad = -2; c._grad = -2; b._grad = -4; a._grad = 6
    
    h = 0.01
    a.data += h * a._grad
    b.data += h * b._grad
    c.data += h * c._grad
    f.data += h * f._grad
    
    e = a * b
    d = e + c
    new_L = f * d
    
    print(new_L)

    
    

if __name__ == '__main__':
    main()
