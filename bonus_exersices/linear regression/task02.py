#linear regression with multiple variables

import pandas as pd
import numpy as np

#loss is 8,95 after both 10_000 and 100_000 epochs. Not great, not terrible?

np.random.seed(45)

def initialize_weight(low : float, high : float) -> float:
    return np.random.uniform(low, high)


def loss_function(bias : float, w1 : float, w2 : float, df : pd.core.frame.DataFrame) -> float:
    sum = 0
    n = df.shape[0]
    
    for row in df.index:
        actual = bias + df['size'][row] * w1 + df['bedrooms'] * w2
        expected = df['price'][row]
        sum += (expected - actual) ** 2
    
    return sum / n
       
        
def main() -> None:
    df = pd.read_csv('/home/deyan/Desktop/ML/bonus_exersices/linear regression/data/ex1data2.txt', sep=',')
    
    learning_rate: float = 0.001
    eps: float = 0.001
    epochs: int = 100
    
    bias: float = initialize_weight(0, 10)
    w1: float = initialize_weight(0, 10)
    w2: float = initialize_weight(0, 10)
    
    print(f'loss before training is: {loss_function(bias, w1, w2, df)}')
    
    for _ in range(epochs):
        bias_der = (loss_function(bias + eps, w1, w2, df) - loss_function(bias, w1, w2, df)) / eps
        w1_der = (loss_function(bias, w1 + eps, w2, df) - loss_function(bias, w1, w2, df)) / eps
        w2_der = (loss_function(bias, w1, w2 + eps, df) - loss_function(bias, w1, w2, df)) / eps
        
        bias -= learning_rate * bias_der
        w1 -= learning_rate * w1_der
        w2  -= learning_rate * w2_der
                
    print(f'loss after training is: {loss_function(bias, w1, w2, df)}')

        
if __name__ == '__main__':
    main()