#linear regression with one variable

import pandas as pd
import numpy as np

#loss is 8,95 after both 10_000 and 100_000 epochs. Not great, not terrible?

np.random.seed(42)

def initialize_weight(low : float, high : float) -> float:
    return np.random.uniform(low, high)


def loss_function(bias : float, w : float, df : pd.core.frame.DataFrame) -> float:
    sum = 0
    n = df.shape[0]
    
    for row in df.index:
        x = bias + df['population'][row] * w
        actual = df[' profit'][row]
        sum += (x - actual) ** 2
    
    return sum / n
       
        
def main() -> None:
    df = pd.read_csv('/home/deyan/Desktop/ML/bonus_exersices/linear regression/data/ex1data1.txt', sep=',')
    
    learning_rate = 0.001
    eps = 0.001
    epochs = 10_000
    
    bias = initialize_weight(0, 10)
    w = initialize_weight(0, 10)
    
    for _ in range(epochs):
        bias_der = (loss_function(bias + eps, w, df) - loss_function(bias, w, df)) / eps
        w_der = (loss_function(bias, w + eps, df) - loss_function(bias, w, df)) / eps
        
        bias -= learning_rate * bias_der
        w -= learning_rate * w_der
                
    print(f'bias: {bias}, w: {w}')
    print(f'loss: {loss_function(bias, w, df)}')
        
if __name__ == '__main__':
    main()