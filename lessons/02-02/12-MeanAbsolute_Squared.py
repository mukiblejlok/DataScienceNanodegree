import numpy as np


def f(x):
    y = 1.2 * x + 2
    return y


def mean_absolute_eror(f, points):
    summed = 0.0
    m = len(points)
    for point in points:
        x, y = point
        yp = f(x)
        summed += np.abs(yp - y)
    return summed / m


def mean_squared_error(f, points):
    summed = 0.0
    m = len(points)
    for point in points:
        x, y = point
        yp = f(x)
        summed += ((yp - y)**2.0)
    return summed / (2.0 * m)


if __name__ == '__main__':

    test_points = [(2, -2), (5, 6), (-4, -4), (-7, 1), (8, 14)]
    mae = mean_absolute_eror(f, test_points)
    mse = mean_squared_error(f, test_points)
    print("MAE", mae)
    print("MSE", mse)





