import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm

from regression import mean_squared_error


def draw_plots(raw_data, std_data, raw_coeff, std_coeff, trail):
    raw_canvas, std_canvas = get_canvases(["Raw data", "Standardized data"])
    loss_canvas = get_canvases(
        ["Loss function"], {"projection": "3d", "computed_zorder": False})

    draw_linear_regression(raw_canvas, raw_data, raw_coeff)
    draw_linear_regression(std_canvas, std_data, std_coeff)
    draw_loss_surface(loss_canvas, std_data, trail)
    plt.show()


def get_canvases(titles, subplot_kw=None):
    """Construct an image with canvases to build plots with."""

    fig, canvas_list = plt.subplots(1, len(titles), subplot_kw=subplot_kw)

    if len(titles) == 1:
        canvas_list.set_title(titles[0])
        return canvas_list

    for canvas, title in zip(canvas_list, titles):
        canvas.set_title(title)
    return canvas_list


def draw_linear_regression(canvas, data, coefficients):
    draw_scatter(canvas, data)
    draw_line(canvas, *coefficients)
    canvas.legend()


def draw_loss_surface(canvas, data, trail):
    draw_surface(canvas, data)
    draw_trail(canvas, trail)
    canvas.legend()


def draw_scatter(ax, data):
    """Draw scatter plot of points on the pandas DataFrame."""

    x_points = data.km.tolist()
    y_points = data.price.tolist()

    ax.scatter(x_points, y_points, label='Data points', color='blue')
    ax.set_xlabel(data.columns[0])
    ax.set_ylabel(data.columns[1])
    ax.grid(True)


def draw_line(ax, intercept, coefficient):
    ax.axline(
        (0, intercept), slope=coefficient, label='Regression line',
        color='orange'
    )


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


def draw_trail(ax, trail):
    x = np.array(trail[0])
    y = np.array(trail[1])
    z = np.array(trail[2])
    ax.scatter(x, y, z, color='black', zorder=1,
               label="Gradient descent trail")
