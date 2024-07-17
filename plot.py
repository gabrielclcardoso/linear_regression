import matplotlib.pyplot as plt


def draw_scatter(ax, data):
    x_points = data.km.tolist()
    y_points = data.price.tolist()

    ax.scatter(x_points, y_points)
    ax.grid(True)


def draw_line(ax, intercept, coefficient):
    ax.axline((0, intercept), slope=coefficient)


def display():
    plt.show()
