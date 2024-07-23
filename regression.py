import numpy as np
import math

MIN_STEP = 1e-6
MAX_ITERATIONS = 1e5
LEARNING_RATE = 0.01


def gradient_descent(data):
    """
    Performs gradient descent on the given data and returns the resulting
    coefficients and a trail of points that the gradient descent passed by.
    The intercept is stored on coefficient[0].
    """

    coefficients = np.array([0, 1], dtype=np.float64)
    step_size = np.array([0, 0], dtype=np.float64)
    x, y, z = [], [], []

    for iteration in range(int(MAX_ITERATIONS)):
        gradient = calculate_gradient(data, coefficients)
        step_size = gradient * LEARNING_RATE
        if np.all(abs(step_size) < MIN_STEP):
            break
        coefficients -= step_size

        if iteration % 100 == 0:
            x.append(coefficients[0])
            y.append(coefficients[1])
            z.append(mean_squared_error(
                coefficients[0], coefficients[1], data))

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


def standardize(data):
    return data.apply(lambda x: (x - x.mean()) / x.std())


def rescale_coefficients(coeff, mean, std_dev):
    rescaled = np.empty([2])
    rescaled[1] = coeff[1] * std_dev.price / std_dev.km
    rescaled[0] = (coeff[0] / std_dev.price) + \
        mean.price - (rescaled[1] * mean.km)
    return rescaled


def print_score(coeff, data):
    rmse = math.sqrt(mean_squared_error(coeff[0], coeff[1], data))
    r_squared = coefficient_of_determination(coeff[0], coeff[1], data)
    print(f'RMSE = {rmse}')
    print(f'R Squared = {r_squared}')


def mean_squared_error(intercept, coefficient, data):
    squared_error = 0
    for car in data.itertuples():
        estimated_price = intercept + coefficient * car.km
        squared_error += (car.price - estimated_price) ** 2
    return squared_error / len(data.index)


def coefficient_of_determination(intercept, coefficient, data):
    predicted_sum = 0
    mean_sum = 0

    for car in data.itertuples():
        estimated_price = intercept + coefficient * car.km
        predicted_sum += (car.price - estimated_price) ** 2
        mean_sum += (car.price - data.price.mean()) ** 2
    return (1 - (predicted_sum / mean_sum))
