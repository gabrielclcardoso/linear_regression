import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm


def get_canvases(titles, subplot_kw=None):
    """Construct an image with canvases to build plots with."""

    fig, canvas_list = plt.subplots(1, len(titles), subplot_kw=subplot_kw)

    if len(titles) == 1:
        canvas_list.set_title(titles[0])
        return canvas_list

    for canvas, title in zip(canvas_list, titles):
        canvas.set_title(title)

    return canvas_list


def draw_scatter(ax, data):
    """Draw scatter plot of points on the pandas DataFrame."""

    x_points = data.km.tolist()
    y_points = data.price.tolist()

    ax.scatter(x_points, y_points, label='Data points', color='blue')
    ax.set_xlabel(data.columns[0])
    ax.set_ylabel(data.columns[1])
    ax.grid(True)
    ax.legend()


def draw_line(ax, intercept, coefficient):
    ax.axline(
        (0, intercept), slope=coefficient, label='Regression line',
        color='orange'
    )
    ax.legend()


def draw_surface(ax, data):
    intercepts = np.arange(-2, 2, 0.1)
    coefficients = np.arange(-2, 2, 0.1)
    intercepts, coefficients = np.meshgrid(intercepts, coefficients)
    loss = mean_squared_error(intercepts, coefficients, data)
    ax.plot_surface(intercepts, coefficients, loss, cmap=cm.Blues, alpha=0.8)


def mean_squared_error(intercept, coefficient, data):
    squared_error = 0
    for car in data.itertuples():
        estimated_price = intercept + coefficient * car.km
        squared_error += (car.price - estimated_price) ** 2
    return squared_error / len(data.index)


def draw_point(ax, x, y, z):
    ax.scatter(x, y, z, color='black', s=10)


def display():
    plt.show()
