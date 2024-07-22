import numpy as np


def standardize(data):
    return data.apply(lambda x: (x - x.mean()) / x.std())


def rescale_coefficients(coeff, mean, std_dev):
    rescaled = np.empty([2])
    rescaled[1] = coeff[1] * std_dev.price / std_dev.km
    rescaled[0] = (coeff[0] / std_dev.price) + \
        mean.price - (rescaled[1] * mean.km)
    return rescaled
