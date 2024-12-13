from functools import cache
from pathlib import Path

input = (Path(__file__).parent / "input.txt").read_text().strip()
stones = list(map(int, input.split(" ")))


@cache
def blink(stone, depth):
    if depth == 0:
        return 1

    if stone == 0:
        return blink(1, depth - 1)
    elif len(str(stone)) % 2 == 0:
        s = str(stone)
        left = blink(int(s[: len(s) // 2]), depth - 1)
        right = blink(int(s[len(s) // 2 :]), depth - 1)
        return left + right
    else:
        return blink(stone * 2024, depth - 1)


print(sum(blink(stone, 25) for stone in stones))
print(sum(blink(stone, 75) for stone in stones))
