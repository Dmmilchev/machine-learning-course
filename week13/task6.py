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
    

def trace_rec(curr : Value, visited : set):
    if len(curr.prev) == 0:
        return set([curr])
    
    visited.add(curr)
    result = set([curr])
    
    for element in curr.prev:
        
        result = result | trace_rec(element, visited)
        
    return result
        
        
def trace(node : Value):
    return trace_rec(node, set([node]))    
    
    
def main() -> None:
    x = Value(2.0)
    y = Value(-3.0)
    z = Value(10.0)
    result = x * y + z

    print(trace(result))
    
main()