import matplotlib.pyplot as plt


def scatter(data):
    x_points = data.km.tolist()
    y_points = data.price.tolist()

    fig, ax = plt.subplots()
    ax.scatter(x_points, y_points)
    ax.grid(True)


def line(intercept, coefficient):
    fig, ax = plt.subplots()
    ax.axline((0, intercept), slope=coefficient)


def draw():
    plt.show()
