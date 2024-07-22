import numpy as np

MIN_STEP = 1e-6
MAX_ITERATIONS = 1e5
LEARNING_RATE = 0.01


def gradient_descent(data):
    """
    Performs gradient descent on the given data and returns the resulting
    coefficients. The intercept is stored on coefficient[0].
    """

    coefficients = np.array([0, 1], dtype=np.float64)
    step_size = np.array([0, 0], dtype=np.float64)
    x, y, z = [], [], []
    for iteration in range(int(MAX_ITERATIONS)):
        gradient = calculate_gradient(data, coefficients)
        step_size = gradient * LEARNING_RATE
        if np.all(abs(step_size) < MIN_STEP):
            break
        if iteration % 100 == 0:
            x.append(coefficients[0])
            y.append(coefficients[1])
            z.append(mean_squared_error(
                coefficients[0], coefficients[1], data))
        coefficients -= step_size
    trail = [x, y, z]
    return coefficients, trail


def calculate_gradient(data, coefficients):
    """
    Calculates gradient for the MSE function with the given coefficients.
    Uses coefficients[0] for the intercept.
    """

    gradient = np.array([0, 0], dtype=np.float64)
    for car in data.itertuples():
        estimated_price = coefficients[0] + coefficients[1] * car.km
        gradient[0] += estimated_price - car.price
        gradient[1] += (estimated_price - car.price) * car.km
    gradient /= len(data.index)
    return gradient


def mean_squared_error(intercept, coefficient, data):
    squared_error = 0
    for car in data.itertuples():
        estimated_price = intercept + coefficient * car.km
        squared_error += (car.price - estimated_price) ** 2
    return squared_error / len(data.index)
