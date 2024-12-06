import re
from pathlib import Path

input = (Path(__file__).parent / "input.txt").read_text().strip()
matches = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", input)
print(sum([int(a) * int(b) for a, b in matches]))

do_indices = [match.start() for match in re.finditer(r"do\(\)", input)]
dont_indices = [match.start() for match in re.finditer(r"don't\(\)", input)]

answer = 0
for match in re.finditer(r"mul\((\d{1,3}),(\d{1,3})\)", input):
    previous_do = next((idx for idx in reversed(do_indices) if idx < match.start()), 0)
    previous_dont = next(
        (idx for idx in reversed(dont_indices) if idx < match.start()),
        -1,
    )
    if previous_do > previous_dont:
        answer += int(match.group(1)) * int(match.group(2))
print(answer)
