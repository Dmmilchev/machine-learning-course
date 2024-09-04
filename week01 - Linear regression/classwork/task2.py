import numpy as np


def create_dataset(n : int) -> list[tuple[int, int]]:
    return [(x, x*2) for x in range(n + 1)]

def initialize_weights(x : int, y : int) -> float:
    return np.random.uniform(x, y)

def calculate_loss(weight : int, dataset : list[tuple[int, int]]) -> float:
    sum = 0
    n = len(dataset)
    for (x, expected) in dataset:
        actual = x * weight
        sum += (actual - expected) ** 2
    return sum / n

def main() -> None:
    training_set = create_dataset(5)
    weight = initialize_weights(0, 10)

    eps = 0.001
    learning_rate = 0.001

    for _ in range(300):
        aproximate_derivative = (calculate_loss(weight + eps, training_set) - calculate_loss(weight, training_set)) / eps
        weight -= learning_rate * aproximate_derivative
        print(f'weight is {weight}')
        print(f'loss is {calculate_loss(weight, training_set)}')
main()