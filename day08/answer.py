from itertools import combinations
from pathlib import Path

import numpy as np

input = (Path(__file__).parent / "input.txt").read_text().strip()
grid = np.array(list(map(list, input.split("\n")))).T
values = np.unique(grid)
values = values[values != "."]

all_antinodes = set()
for value in values:
    indices = np.argwhere(grid == value)
    for i, j in combinations(indices, 2):
        antinodes = np.stack([2 * i - j, 2 * j - i])
        antinodes = antinodes[
            np.all(antinodes >= 0, axis=1) & np.all(antinodes < grid.shape, axis=1)
        ]
        all_antinodes.update(map(tuple, antinodes.tolist()))

print(len(all_antinodes))

all_antinodes = set()
for value in values:
    indices = np.argwhere(grid == value)
    for i, j in combinations(indices, 2):
        antinodes = np.stack(
            [i - k * (j - i) for k in range(grid.shape[0])]
            + [j + k * (j - i) for k in range(grid.shape[0])]
        )
        antinodes = antinodes[
            np.all(antinodes >= 0, axis=1) & np.all(antinodes < grid.shape, axis=1)
        ]
        all_antinodes.update(map(tuple, antinodes.tolist()))

print(len(all_antinodes))
