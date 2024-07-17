import pandas as pd
import numpy as np
import sys

MIN_STEP = 1e-3  # What value should be put here?
MAX_ITERATIONS = 1e4  # What value shoud be put here?
LEARNING_RATE = 0.0000000001  # What value shoud be put here?


def main():
    data = read_data()
    coefficients = gradient_descent(data)
    save_coefficients(coefficients)


def read_data():
    try:
        data = pd.read_csv('data.csv')
        return data
    except Exception as e:
        print(e, file=sys.stderr)
        exit(1)


def gradient_descent(data):
    coefficients = np.array([0, 1], dtype=np.float64)
    step_size = np.array([0, 0], dtype=np.float64)
    for iteration in range(int(MAX_ITERATIONS)):
        gradient = calculate_gradient(data, coefficients)
        step_size = gradient * LEARNING_RATE
        if np.all(abs(step_size) < MIN_STEP):
            break
        coefficients -= step_size
    return coefficients


def calculate_gradient(data, coefficients):
    gradient = np.array([0, 0], dtype=np.float64)
    for car in data.itertuples():
        estimated_price = coefficients[0] + coefficients[1] * car.km
        gradient[0] += estimated_price - car.price
        gradient[1] += (estimated_price - car.price) * car.km
    gradient /= len(data.index)
    return gradient


def save_coefficients(coefficients):
    try:
        file = open('coefficients.bin', 'wb')
    except Exception as e:
        print(e, file=sys.stderr)
        exit(1)
    coefficients.tofile(file)
    file.close()


if __name__ == '__main__':
    main()
