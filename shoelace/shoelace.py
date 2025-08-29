import numpy as np

def shoelace_formula(boundary_points, absoluteValue=True):
    points = np.array(boundary_points)
    x = points[:, 0]
    y = points[:, 1]

    area = 0.5 * np.sum(x * np.roll(y, -1) - y * np.roll(x, -1))

    return abs(area) if absoluteValue else area

square = [(0,0), (1,0), (1,1), (0,1)]
print(shoelace_formula(square))
