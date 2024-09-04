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
    
    
def mat_add(mat1 : Mat , mat2 : Mat) -> Mat:
        return np.add(mat1.mat, mat2.mat)
    
def mat_mult(mat1 : Mat , mat2 : Mat) -> Mat:
        return np.multiply(mat1.mat, mat2.mat)
    

def main() -> None:
    w1 = Mat(2, 2)
    w2 = Mat(2, 2)

    w1.set_at(0, 0, 1)
    w1.set_at(0, 1, 2)
    w1.set_at(1, 0, 3)
    w1.set_at(1, 1, 4)

    w2.set_at(0, 0, 5)
    w2.set_at(0, 1, 6)
    w2.set_at(1, 0, 7)
    w2.set_at(1, 1, 8)

    print(f'Result of addition: {mat_add(w1, w2)}')
    print(f'Result of multiplication: {mat_mult(w1, w2)}')
        
    
if __name__ == '__main__':
    main()
