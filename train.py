import pandas as pd
import numpy as np
import sys

MIN_STEP = 1e-3  # What value should be put here?
MAX_ITERATIONS = 10e5  # What value shoud be put here?
LEARNING_RATE = 0.1  # What value shoud be put here?


def main():
    # Read Database
    try:
        data = pd.read_csv('data.csv')
    except Exception as e:
        print(e, file=sys.stderr)
        exit(1)

    # Perform gradien descent
    thetha = np.array([0.0, 1])
    step_size = np.array([0.0, 0])
    for iteration in range(int(MAX_ITERATIONS)):
        gradient = calculate_gradient(data, thetha)
        step_size[0] = LEARNING_RATE * gradient[0]
        step_size[1] = LEARNING_RATE * gradient[1]
        if np.any(step_size < MIN_STEP):
            break
        thetha[0] -= step_size[0]
        thetha[1] -= step_size[1]
    print(f'0 = {thetha[0]} | 1 = {thetha[1]}')  # Save to file afterwards


def calculate_gradient(data, thetha):
    gradient = np.array([0.0, 0])
    for car in data.itertuples():
        estimated_price = thetha[0] + thetha[1] * car.km
        gradient[0] += estimated_price - car.price
        gradient[1] += (estimated_price - car.price) * car.km
    return (gradient / len(data.index))


if __name__ == '__main__':
    main()
