from pathlib import Path

import numpy as np

input = (Path(__file__).parent / "input.txt").read_text().strip()
input = list(map(int, input))

files = input[::2]
free = input[1::2]
total_free = sum(free)

ids = [
    i if x < j else "."
    for i, (j, k) in enumerate(zip(files + [0], free + [0]))
    for x in range(j + k)
]

j = len(ids) - 1
for id in range(0, len(ids)):
    if ids[id] == ".":
        while ids[j] == ".":
            j -= 1
        if j <= id:
            break
        ids[id], ids[j] = ids[j], ids[id]

checksum = 0
for id, x in enumerate(ids[:-total_free]):
    if x == ".":
        continue
    checksum += id * x
print("Checksum:", checksum)

indices = [0] + np.cumsum(input)[:-1].tolist()
file_indices = indices[::2]
free_indices = indices[1::2]

for id in range(len(files) - 1, -1, -1):
    file_count = files[id]
    file_index = file_indices[id]
    free_count_index = next((i for i in range(len(free)) if free[i] >= file_count), -1)
    if free_count_index == -1:
        continue
    free_count = free[free_count_index]
    free_index = free_indices[free_count_index]
    if free_index > file_index:
        continue
    file_indices[id] = free_index
    free[free_count_index] -= file_count
    free_indices[free_count_index] += file_count

checksum = 0
for id in range(len(files)):
    for index in range(file_indices[id], file_indices[id] + files[id]):
        checksum += id * index
print("Checksum:", checksum)
