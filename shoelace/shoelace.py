import numpy as np

def shoelace_formula(boundary_points, absoluteValue=True):
    x, y = zip(*boundary_points)
    len_x = len(x)
    len_y = len(y)

    if len_x != len_y:
        raise SystemExit("Lengths of x and y must be equal")

    sum_one = 0
    sum_two = 0
    for i in range(len_x-1):
        sum_one = sum_one + (x[i] * y[i+1])
        sum_two = sum_two + (y[i]*x[i+1])

    if absoluteValue:
        return abs(sum_one-sum_two)

    return (sum_one-sum_two)


