from time import perf_counter

import numpy as np
from numpy.typing import NDArray

from src.plotting import plot_points


def convex_bucket(points: NDArray) -> NDArray:
    """Complexity: O(n log n)"""
    # Sort by x-coord then by y-coord
    points = points[np.lexsort((points[:, 1], points[:, 0]))]

    lower_envelope = [points[0]]

    for i in range(1, len(points)):
        while len(lower_envelope) >= 2 and np.cross(lower_envelope[-2] - lower_envelope[-1], points[i] - lower_envelope[-1]) >= 0:
            lower_envelope.pop()

        lower_envelope.append(points[i])

    return np.array(lower_envelope + lower_envelope[::-1])


if __name__ == "__main__":
    for i in range(1, 11):
        txtpath = f"../points_{i}.txt"
        points = np.loadtxt(txtpath)
        print(f"Processing {txtpath}")
        print("-" * 32)
        t_start = perf_counter()
        ch = convex_bucket(points)
        t_end = perf_counter()
        print(f"Elapsed time: {t_end - t_start} sec")
        plot_points(points, convex_hull=ch, markersize=20)
        print()
