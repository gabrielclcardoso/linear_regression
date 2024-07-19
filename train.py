import pandas as pd
import sys

import plot as plot
import standardization as std
from regression import gradient_descent

MIN_STEP = 1e-6  # What value should be put here?
MAX_ITERATIONS = 1e4  # What value shoud be put here?
LEARNING_RATE = 0.001  # What value shoud be put here?


def main():
    data = read_data()

    raw_canvas, std_canvas = plot.get_canvases(
        ["Raw data", "Standardized data"])
    loss_canvas = plot.get_canvases(["Loss function"], {"projection": "3d"})

    plot.draw_scatter(raw_canvas, data)

    mean, std_deviation = std.get_mean_and_deviation(data)
    std.standardize(data, mean, std_deviation)

    plot.draw_scatter(std_canvas, data)
    plot.draw_surface(loss_canvas, data)

    coefficients, trail = gradient_descent(data, loss_canvas)
    plot.draw_trail(loss_canvas, trail)
    plot.draw_line(std_canvas, *coefficients)

    std.rescale_coefficients(coefficients, mean, std_deviation)
    plot.draw_line(raw_canvas, *coefficients)

    save_coefficients(coefficients)
    plot.display()


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
