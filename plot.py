import matplotlib.pyplot as plt


def get_canvases(n):
    """Construct n canvases to build plots with."""

    fig, canvas_list = plt.subplots(1, n)
    return canvas_list


def draw_scatter(ax, data):
    """Draw scatter plot of points on the pandas DataFrame."""

    x_points = data.km.tolist()
    y_points = data.price.tolist()

    ax.scatter(x_points, y_points)
    ax.grid(True)


def draw_line(ax, intercept, coefficient):
    ax.axline((0, intercept), slope=coefficient)


def display():
    plt.show()
