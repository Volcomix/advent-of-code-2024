from pathlib import Path

input = (Path(__file__).parent / "input.txt").read_text().strip()
operators = []
for line in input.split("\n"):
    result, values = line.split(": ")
    result = int(result)
    values = list(map(int, values.split(" ")))
    operators.append((result, values))


def combinations(count):
    for i in range(2**count):
        yield [i & (1 << j) != 0 for j in range(count)]


total_calibration_result = 0
for result, values in operators:
    for c in combinations(len(values) - 1):
        r = values[0]
        for i, v in enumerate(values[1:]):
            if c[i]:
                r += v
            else:
                r *= v
        if r == result:
            total_calibration_result += result
            break

print(total_calibration_result)
