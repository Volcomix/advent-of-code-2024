from functools import cache
from pathlib import Path

import numpy as np

input = (Path(__file__).parent / "input.txt").read_text().strip()
operators = []
for line in input.split("\n"):
    result, values = line.split(": ")
    result = int(result)
    values = list(map(int, values.split(" ")))
    operators.append((result, values))


@cache
def combinations2(count):
    return [[i & (1 << j) != 0 for j in range(count)] for i in range(2**count)]


total_calibration_result = 0
for result, values in operators:
    for c in combinations2(len(values) - 1):
        r = values[0]
        for i, v in enumerate(values[1:]):
            if c[i]:
                r += v
            else:
                r *= v
            if r > result:
                break
        if r == result:
            total_calibration_result += result
            break

print(total_calibration_result)


@cache
def combinations3(count):
    return [
        [int(c) for c in np.base_repr(i, base=3).rjust(count, "0")]
        for i in range(3**count)
    ]


total_calibration_result = 0
for i, (result, values) in enumerate(operators):
    print(f"{i + 1} / {len(operators)}")
    for c in combinations3(len(values) - 1):
        r = values[0]
        for i, v in enumerate(values[1:]):
            if c[i] == 0:
                r += v
            elif c[i] == 1:
                r *= v
            elif c[i] == 2:
                r = int(f"{r}{v}")
            if r > result:
                break
        if r == result:
            total_calibration_result += result
            break

print(total_calibration_result)
