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
    
def mat_sig(mat : Mat) -> Mat:
    def sigmoid(x):
        return 1/(1 + np.exp(-x))
    
    return np.apply_along_axis(sigmoid, 1, mat.mat)


def main() -> None:
    np.random.seed(42)

    w1 = Mat(2, 2)
    w2 = Mat(2, 2)

    w1.randomize(0, 10)
    w2.randomize(0, 10)

    print(mat_sig(w1))
    print(mat_sig(w2))
    
    
if __name__ == '__main__':
    main()
