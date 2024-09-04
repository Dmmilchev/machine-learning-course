import numpy as np

#this model has 2 parameters w1 and w2
#the general form is: y = x*w1 + y*w2

def create_dataset_and() -> list[(int, int, int)]:
   return [(0, 0, 0), 
           (0, 1, 0), 
           (1, 0, 0),
           (1, 1, 1)]

def create_dataset_or() -> list[(int, int, int)]:
    return [(0, 0, 0), 
            (0, 1, 1), 
            (1, 0, 1),
            (1, 1, 1)]
 
def initialize_weights(x : int, y : int) -> float:
    return np.random.uniform(x, y)

def calculate_loss(w1 : int, w2 : int, dataset : list[(int, int, int)]) -> float:
    sum = 0
    n = len(dataset)
    for (x, y, expected) in dataset:
        actual = x*w1 + y*w2
        sum += (actual - expected) ** 2
    return sum / n

def main() -> None:
    and_dataset = create_dataset_and()
    w1= initialize_weights(0, 3)
    w2 = initialize_weights(0, 3)

    eps = 0.001
    learning_rate = 0.001
    epochs = 100_000

    for _ in range(epochs):
        der_loss_w1 = (calculate_loss(w1 + eps, w2, and_dataset) - calculate_loss(w1, w2, and_dataset))/eps
        der_loss_w2 = (calculate_loss(w1, w2 + eps, and_dataset) - calculate_loss(w1, w2, and_dataset))/eps
        
        w1 -= learning_rate * der_loss_w1
        w2 -= learning_rate * der_loss_w2
    
    print(f'loss now is: {calculate_loss(w1, w2, and_dataset)} for and prediction')
    print('and predictions:')
    for i in range(2):
        for j in range(2):
            print(i, j, w1 * i + w2 * j)

    or_dataset = create_dataset_or()
    w1= initialize_weights(0, 3)
    w2 = initialize_weights(0, 3)
  
    for _ in range(epochs):
        der_loss_w1 = (calculate_loss(w1 + eps, w2, or_dataset) - calculate_loss(w1, w2, or_dataset))/eps
        der_loss_w2 = (calculate_loss(w1, w2 + eps, or_dataset) - calculate_loss(w1, w2, or_dataset))/eps

        w1 -= learning_rate * der_loss_w1
        w2 -= learning_rate * der_loss_w2  

    print(f'loss now is: {calculate_loss(w1, w2, or_dataset)} for or prediction')
    print('or predictions:')
    for i in range(2):
        for j in range(2):
            print(i, j, w1 * i + w2 * j)
    
if __name__ == '__main__':
    main()