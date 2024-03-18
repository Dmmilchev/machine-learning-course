import numpy as np


class Mat:
    def __init__(self, rows : int, cols : int) -> None:
        self.mat = np.zeros((rows, cols))
        
        
    def set_at(self, row : int, col : int, number : float) -> None:
        if row >= self.mat.shape[0] or col >= self.mat.shape[1]:
            raise IndexError('Invalid row or col index')
        
        self.mat[row, col] = number
        
    
    def randomize(self, low : float, high : float) -> None:
        self.mat = np.random.uniform(low, high, size = (self.mat.shape[0], self.mat.shape[1]))
        
        
    def __repr__(self) -> str:
        return self.mat.__repr__()



def main() -> None:
    np.random.seed(42)

    inp = Mat(1, 2)
    w1 = Mat(2, 2)
    b1 = Mat(1, 2)
    w2 = Mat(2, 1)
    b2 = Mat(1, 1)

    inp.set_at(0, 0, 0)
    inp.set_at(0, 1, 1)

    w1.randomize(0, 1)
    b1.randomize(0, 1)
    w2.randomize(0, 1)
    b2.randomize(0, 1)

    print(inp)
    print(w1)
    print(b1)
    print(w2)
    print(b2)
    
    
if __name__ == '__main__':
    main()
