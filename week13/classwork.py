class Value:
    def __init__(self, number : float) -> None:
        self.number = number
        
    def __repr__(self) -> str:
        return f'Value(data={self.number})'
    
    def __add__(self, other):
        return Value(self.number + other.number)
    

def main() -> None:
    value1 = Value(5)
    print(value1)
    
    value2 = Value(100)
    print(value2)

    value3 = value1 + value2
    print(value3)
    
    
main()