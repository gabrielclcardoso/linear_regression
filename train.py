import pandas as pd
import sys

import standardization as std
from plot import draw_plots
from regression import gradient_descent


def main():
    raw_data = read_data()
    std_data = std.standardize(raw_data)

    coefficients, trail = gradient_descent(std_data)
    rescaled_coefficients = std.rescale_coefficients(
        coefficients, raw_data.mean(), raw_data.std())

    save_coefficients(rescaled_coefficients)
    draw_plots(raw_data, std_data, rescaled_coefficients, coefficients, trail)


def read_data():
    """Read and return the dataset from the data.csv file."""

    try:
        data = pd.read_csv('data.csv')
        return data
    except Exception as e:
        print(e, file=sys.stderr)
        exit(1)


def save_coefficients(coefficients):
    """Save coefficient values into binary file."""

    try:
        file = open('coefficients.bin', 'wb')
    except Exception as e:
        print(e, file=sys.stderr)
        exit(1)
    coefficients.tofile(file)
    file.close()


if __name__ == '__main__':
    main()
