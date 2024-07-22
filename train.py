import pandas as pd
import sys

import plot as plot
import standardization as std
from regression import gradient_descent


def main():
    raw_data = read_data()

    raw_canvas, std_canvas = plot.get_canvases(
        ["Raw data", "Standardized data"])
    loss_canvas = plot.get_canvases(
        ["Loss function"], {"projection": "3d", "computed_zorder": False})

    plot.draw_scatter(raw_canvas, raw_data)

    std_data = std.standardize(raw_data)

    plot.draw_scatter(std_canvas, std_data)
    plot.draw_surface(loss_canvas, std_data)

    coefficients, trail = gradient_descent(std_data, loss_canvas)
    plot.draw_trail(loss_canvas, trail)
    plot.draw_line(std_canvas, *coefficients)

    rescaled_coefficients = std.rescale_coefficients(
        coefficients, raw_data.mean(), raw_data.std())
    plot.draw_line(raw_canvas, *rescaled_coefficients)

    save_coefficients(rescaled_coefficients)
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
