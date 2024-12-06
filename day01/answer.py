from pathlib import Path

import numpy as np

input = (Path(__file__).parent / "input.txt").read_text().strip()

left = []
right = []
for line in input.split("\n"):
    ids = list(map(int, line.split(" " * 3)))
    left.append(ids[0])
    right.append(ids[1])
left.sort()
right.sort()

distances = []
for left_id, right_id in zip(left, right):
    distances.append(abs(left_id - right_id))

print(sum(distances))

right_array = np.array(right)

print(sum(left_id * right.count(left_id) for left_id in left))
