import numpy as np


def find_pair(data, w):
    # First, replace outliers in data with zeros.
    data = np.array(data)
    w = np.array(w)
    for i, row in enumerate(data):
        mean = np.average(row, weights=w)
        std = np.sqrt(np.average((row - mean) ** 2, weights=w))
        outliers = (row < mean - 2 * std) | (row > mean + 2 * std)
        data[i, outliers] = 0

    # Now, calculate the weighted covariance and correlation for each pair of stocks.
    num_stocks = len(data)
    max_corr = 0
    max_pair = (0, 1)

    for i in range(num_stocks):
        for j in range(i + 1, num_stocks):
            # Calculate weighted means
            mean_i = np.average(data[i], weights=w)
            mean_j = np.average(data[j], weights=w)

            # Calculate weighted covariance
            covariance = np.average((data[i] - mean_i) * (data[j] - mean_j), weights=w)

            # Calculate variances
            variance_i = np.average((data[i] - mean_i) ** 2, weights=w)
            variance_j = np.average((data[j] - mean_j) ** 2, weights=w)

            # Calculate correlation
            correlation = covariance / np.sqrt(variance_i * variance_j)

            # Check if this is the highest absolute correlation so far
            if abs(correlation) > max_corr:
                max_corr = abs(correlation)
                max_pair = (i, j)

    return max_pair


# Test the function
data = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 300],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 0],
    [-5, -4, 3, 4, 5, 6, 7, 8, 9, -300]
]
w = [100, 100, 100, 100, 1, 1, 1, 1, 1, 1]

# Execute the function
print(find_pair(data, w))
