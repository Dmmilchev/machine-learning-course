import numpy as np
import copy


np.random.seed(42)


def initialize_dataset() -> list[(int, int, int)]:
    return [(0, 0, 0), 
            (0, 1, 1), 
            (1, 0, 1),
            (1, 1, 0)]


class Xor:
    def __init__(self) -> None:
        self.or_bias: float = 0
        self.or_w1: float = 0
        self.or_w2: float = 0
        
        self.nand_bias: float = 0
        self.nand_w1: float = 0
        self.nand_w2: float = 0
        
        self.and_bias: float = 0
        self.and_w1: float = 0
        self.and_w2: float = 0
        
    #I don't know how to use type hints for custom classes?
    #Tried searching in stackoverflow, but could not find anything useful
    def initialize_weights(self, low : float, high : float):
        obj = Xor()
        
        obj.or_bias = np.random.uniform(low, high)
        obj.or_w1 = np.random.uniform(low, high)
        obj.or_w2 = np.random.uniform(low, high)
        
        obj.nand_bias = np.random.uniform(low, high)
        obj.nand_w1 = np.random.uniform(low, high)
        obj.nand_w2 = np.random.uniform(low, high)
        
        obj.and_bias = np.random.uniform(low, high)
        obj.and_w1 = np.random.uniform(low, high)
        obj.and_w2 = np.random.uniform(low, high)
        
        return obj
        
        
def sigmoid(x : float) -> float:
        return 1 / (1 + np.exp(-x))
        
        
def forward(xor,  x : int, y : int) -> float:
    x2 = (xor.or_bias + xor.or_w1*x + xor.or_w2*y)
    y2 = (xor.nand_bias + xor.nand_w1*x + xor.nand_w2*y)
    return (xor.and_bias + xor.and_w1*x2 + xor.and_w2*y2)


def calculate_loss(xor, data : list[(int, int, int)]) -> float:
    sum = 0
    n = len(data)
    
    for x, y, expected in data:
        actual = forward(xor, x, y)
        sum += (expected - actual) ** 2
    
    return sum / n


def modify(xor, learning_rate, eps, dataset):
    #initializing epsilon change in parameters
    eps_or_bias = copy.deepcopy(xor)
    eps_or_bias.or_bias += eps
    eps_or_w1 = copy.deepcopy(xor)
    eps_or_w1.or_w1 += eps
    eps_or_w2 = copy.deepcopy(xor)
    eps_or_w2.or_w2 += eps

    eps_nand_bias = copy.deepcopy(xor)
    eps_nand_bias.nand_bias += eps
    eps_nand_w1 = copy.deepcopy(xor)
    eps_nand_w1.nand_w1 += eps
    eps_nand_w2 = copy.deepcopy(xor)
    eps_nand_w2.nand_w2 += eps
    
    eps_and_bias = copy.deepcopy(xor)
    eps_and_bias.and_bias += eps
    eps_and_w1 = copy.deepcopy(xor)
    eps_and_w1.and_w1 += eps
    eps_and_w2 = copy.deepcopy(xor)
    eps_and_w2.and_w2 += eps

    #calculating derivative
    der_or_bias = (calculate_loss(eps_or_bias, dataset) - calculate_loss(xor, dataset)) / eps
    der_or_w1 = (calculate_loss(eps_or_w1, dataset) - calculate_loss(xor, dataset)) / eps
    der_or_w2 = (calculate_loss(eps_or_w2, dataset) - calculate_loss(xor, dataset)) / eps
    
    der_nand_bias = (calculate_loss(eps_nand_bias, dataset) - calculate_loss(xor, dataset)) / eps
    der_nand_w1 = (calculate_loss(eps_nand_w1, dataset) - calculate_loss(xor, dataset)) / eps
    der_nand_w2 = (calculate_loss(eps_nand_w2, dataset) - calculate_loss(xor, dataset)) / eps
    
    der_and_bias = (calculate_loss(eps_and_bias, dataset) - calculate_loss(xor, dataset)) / eps
    der_and_w1 = (calculate_loss(eps_and_w1, dataset) - calculate_loss(xor, dataset)) / eps
    der_and_w2 = (calculate_loss(eps_and_w2, dataset) - calculate_loss(xor, dataset)) / eps
    
    #initializing the new model
    new_model = Xor()
    new_model.or_bias = xor.or_bias - learning_rate * der_or_bias
    new_model.or_w1 = xor.or_w1 - learning_rate * der_or_w1
    new_model.or_w2 = xor.or_w2 - learning_rate * der_or_w2
    
    new_model.nand_bias = xor.nand_bias - learning_rate * der_nand_bias
    new_model.nand_w1 = xor.nand_w1 - learning_rate * der_nand_w1
    new_model.nand_w2 = xor.nand_w2 - learning_rate * der_nand_w2

    new_model.and_bias = xor.and_bias - learning_rate * der_and_bias
    new_model.and_w1 = xor.and_w1 - learning_rate * der_and_w1
    new_model.and_w2 = xor.and_w2 - learning_rate * der_and_w2
    
    return new_model
   


def main() -> None:
    xor = Xor()
    xor = xor.initialize_weights(0, 10)
    
    dataset = initialize_dataset()
    
    eps = 0.001
    learning_rate = 0.001
    epochs = 10_000
    
    print(f'loss before training is: {calculate_loss(xor, dataset)}')
    
    for _ in range(epochs):
        xor = modify(xor, learning_rate, eps, dataset)
    
    print(f'loss after training is: {calculate_loss(xor, dataset)}')
    
    
if __name__ == '__main__':
    main()