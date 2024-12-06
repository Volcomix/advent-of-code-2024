from pathlib import Path

import numpy as np

input = (Path(__file__).parent / "input.txt").read_text().strip()

reports = []
for line in input.split("\n"):
    reports.append(list(map(int, line.split(" "))))


def is_safe(report):
    if report != sorted(report) and report != sorted(report, reverse=True):
        return False
    np_report = np.array(report)
    diff = np.abs(np_report[:-1] - np_report[1:])
    if (diff < 1).any() or (diff > 3).any():
        return False
    return True


safe = []
for report in reports:
    if is_safe(report):
        safe.append(report)

print(len(safe))


def all_combinations(report):
    yield report
    for i in range(len(report)):
        yield report[:i] + report[i + 1 :]


safe = []
for report in reports:
    if any(map(is_safe, all_combinations(report))):
        safe.append(report)

print(len(safe))
