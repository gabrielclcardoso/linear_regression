def get_mean_and_deviation(data):
    return [data.mean(), data.std()]


def standardize(data, mean, std_deviation):
    for col in data.columns:
        data[col] = (data[col] - mean[col]) / std_deviation[col]


def rescale_coefficients(coeff, mean, std_dev):
    coeff[1] *= std_dev.price / std_dev.km
    coeff[0] = (coeff[0] / std_dev.price) + mean.price - (coeff[1] * mean.km)
