def get_mean_and_deviation(data):
    return [data.mean(), data.std()]


def standardize(data, mean, std_deviation):
    for col in data.columns:
        data[col] = (data[col] - mean[col]) / std_deviation[col]
