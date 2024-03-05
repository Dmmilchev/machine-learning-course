import numpy as np

def create_nand_training_set() -> list[(int, int, int)]:
    return [(0, 0, 1),
            (0, 1, 1),
            (1, 0, 1),
            (1, 1, 0)]
    
def initialize_weights(low : float, high : float) -> float:
    return np.random.uniform(low, high)

def calculate_loss(w1 : float, w2 : float, bias : float, training_set : list[(int, int, int)]) -> float:
    sum = 0
    n = len(training_set)
    
    for x, y, expected in training_set:
        actual = bias + w1*x + w2*y
        sum += (actual - expected)**2
        
    return sum / n

def main() -> None:
    nand_training_set = create_nand_training_set()
    bias, w1, w2 = initialize_weights(0, 2), initialize_weights(0, 2), initialize_weights(0, 2)

    eps = 0.001
    learning_rate = 0.001
    epochs = 10000
    
    for _ in range(epochs):
        der_loss_w1 = (calculate_loss(w1 + eps, w2, bias, nand_training_set) - calculate_loss(w1, w2, bias, nand_training_set))/eps
        der_loss_w2 = (calculate_loss(w1, w2 + eps, bias, nand_training_set) - calculate_loss(w1, w2, bias, nand_training_set))/eps
        der_loss_bias = (calculate_loss(w1, w2, bias + eps, nand_training_set) - calculate_loss(w1, w2, bias, nand_training_set))/eps

        w1 -= learning_rate * der_loss_w1
        w2 -= learning_rate * der_loss_w2
        bias -= learning_rate * der_loss_bias
    
    print(f'loss now is: {calculate_loss(w1, w2, bias, nand_training_set)} for and prediction')
    print('nand predictions:')
    for i in range(2):
        for j in range(2):
            print(i, j, w1 * i + w2 * j + bias)
            
if __name__ == '__main__':
    main()