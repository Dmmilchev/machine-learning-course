import numpy as np
import matplotlib.pyplot as plt

#Here we plot how loss is changing with every epoch. We are using sigmoid function here.

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


def calculate_loss(w1 : int, w2 : int, bias : int, dataset : list[(int, int, int)]) -> float:
    sum = 0
    n = len(dataset)
    for (x, y, expected) in dataset:
        actual = x*w1 + y*w2 + bias
        sum += (actual - expected) ** 2
    return sum / n


def main() -> None:
    and_dataset = create_dataset_and()
    w1= initialize_weights(0, 3)
    w2 = initialize_weights(0, 3)
    bias = initialize_weights(0, 3)

    eps = 0.001
    learning_rate = 0.001
    epochs = 10_000
    plot_x = []
    plot_y = []

    for epoch in range(epochs):
        der_loss_w1 = (calculate_loss(w1 + eps, w2, bias, and_dataset) - calculate_loss(w1, w2, bias, and_dataset))/eps
        der_loss_w2 = (calculate_loss(w1, w2 + eps, bias, and_dataset) - calculate_loss(w1, w2, bias, and_dataset))/eps
        der_loss_bias = (calculate_loss(w1, w2, bias + eps, and_dataset) - calculate_loss(w1, w2, bias, and_dataset))/eps

        w1 -= learning_rate * der_loss_w1
        w2 -= learning_rate * der_loss_w2
        bias -= learning_rate * der_loss_bias
        
        plot_x.append(epoch)
        plot_y.append(calculate_loss(w1, w2, bias, and_dataset))
    
    print(f'loss now is: {calculate_loss(w1, w2, bias, and_dataset)} for and prediction')
    print('and predictions:')
    for i in range(2):
        for j in range(2):
            print(i, j, w1 * i + w2 * j + bias)

    fig = plt.figure()
    axes = fig.add_axes([0, 0, 1, 1])
    axes.plot(plot_x, plot_y, color = 'blue')
    plt.show()
    
    
if __name__ == '__main__':
    main()
    
    