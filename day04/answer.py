from pathlib import Path

input = (Path(__file__).parent / "input.txt").read_text().strip()

grid = input.split("\n")


def check_letter(row, col, letter):
    if row < 0 or row >= len(grid):
        return False
    if col < 0 or col >= len(grid[row]):
        return False
    return grid[row][col] == letter


count = 0
for row in range(len(grid)):
    for col in range(len(grid[row])):
        if not check_letter(row, col, "X"):
            continue

        # Check XMAS horizontally to the right
        if (
            check_letter(row, col + 1, "M")
            and check_letter(row, col + 2, "A")
            and check_letter(row, col + 3, "S")
        ):
            count += 1

        # Check XMAS horizontally to the left
        if (
            check_letter(row, col - 1, "M")
            and check_letter(row, col - 2, "A")
            and check_letter(row, col - 3, "S")
        ):
            count += 1

        # Check XMAS vertically down
        if (
            check_letter(row + 1, col, "M")
            and check_letter(row + 2, col, "A")
            and check_letter(row + 3, col, "S")
        ):
            count += 1

        # Check XMAS vertically up
        if (
            check_letter(row - 1, col, "M")
            and check_letter(row - 2, col, "A")
            and check_letter(row - 3, col, "S")
        ):
            count += 1

        # Check XMAS diagonally down-right
        if (
            check_letter(row + 1, col + 1, "M")
            and check_letter(row + 2, col + 2, "A")
            and check_letter(row + 3, col + 3, "S")
        ):
            count += 1

        # Check XMAS diagonally down-left
        if (
            check_letter(row + 1, col - 1, "M")
            and check_letter(row + 2, col - 2, "A")
            and check_letter(row + 3, col - 3, "S")
        ):
            count += 1

        # Check XMAS diagonally up-right
        if (
            check_letter(row - 1, col + 1, "M")
            and check_letter(row - 2, col + 2, "A")
            and check_letter(row - 3, col + 3, "S")
        ):
            count += 1

        # Check XMAS diagonally up-left
        if (
            check_letter(row - 1, col - 1, "M")
            and check_letter(row - 2, col - 2, "A")
            and check_letter(row - 3, col - 3, "S")
        ):
            count += 1
print(count)


def check_xmas1(row, col):
    if not check_letter(row, col, "A"):
        return False
    if not check_letter(row - 1, col - 1, "M"):
        return False
    if not check_letter(row - 1, col + 1, "S"):
        return False
    if not check_letter(row + 1, col - 1, "M"):
        return False
    if not check_letter(row + 1, col + 1, "S"):
        return False
    return True


def check_xmas2(row, col):
    if not check_letter(row, col, "A"):
        return False
    if not check_letter(row - 1, col - 1, "S"):
        return False
    if not check_letter(row - 1, col + 1, "M"):
        return False
    if not check_letter(row + 1, col - 1, "S"):
        return False
    if not check_letter(row + 1, col + 1, "M"):
        return False
    return True


def check_xmas3(row, col):
    if not check_letter(row, col, "A"):
        return False
    if not check_letter(row - 1, col - 1, "M"):
        return False
    if not check_letter(row - 1, col + 1, "M"):
        return False
    if not check_letter(row + 1, col - 1, "S"):
        return False
    if not check_letter(row + 1, col + 1, "S"):
        return False
    return True


def check_xmas4(row, col):
    if not check_letter(row, col, "A"):
        return False
    if not check_letter(row - 1, col - 1, "S"):
        return False
    if not check_letter(row - 1, col + 1, "S"):
        return False
    if not check_letter(row + 1, col - 1, "M"):
        return False
    if not check_letter(row + 1, col + 1, "M"):
        return False
    return True


count = 0
for row in range(len(grid)):
    for col in range(len(grid[row])):
        if (
            check_xmas1(row, col)
            or check_xmas2(row, col)
            or check_xmas3(row, col)
            or check_xmas4(row, col)
        ):
            count += 1
print(count)
