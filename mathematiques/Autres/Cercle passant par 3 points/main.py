import numpy as np


def cercle_passant_par_3_points(p1, p2, p3):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3

    A = np.array([[x1 - x2, y1 - y2],
                  [x1 - x3, y1 - y3]])
    B = np.array([0.5 * ((x1**2 - x2**2) + (y1**2 - y2**2)),
                  0.5 * ((x1**2 - x3**2) + (y1**2 - y3**2))])

    cx, cy = np.linalg.solve(A, B)
    r = np.sqrt((cx - x1)**2 + (cy - y1)**2)

    return (cx, cy), r