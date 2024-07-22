import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm

from regression import mean_squared_error


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
    ax.set_xlabel("Intercept")
    ax.set_ylabel("Coefficient")
    ax.set_zlabel("MSE")
    ax.plot_surface(intercepts, coefficients, loss, label="MSE surface",
                    cmap=cm.Blues, zorder=0)
    ax.legend()


def draw_trail(ax, trail):
    x = np.array(trail[0])
    y = np.array(trail[1])
    z = np.array(trail[2])
    ax.scatter(x, y, z, color='black', zorder=1,
               label="Gradient descent trail")
    ax.legend()


def display():
    plt.show()
