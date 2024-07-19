import matplotlib.pyplot as plt


def get_canvases(titles):
    """Construct n canvases to build plots with."""

    fig, canvas_list = plt.subplots(1, len(titles))
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


def display():
    plt.show()
