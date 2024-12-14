from pathlib import Path

input = (Path(__file__).parent / "input.txt").read_text().strip()
grid = input.split("\n")


def neighbors(cell):
    row, col = cell
    if row > 0:
        yield (row - 1, col)
    if col > 0:
        yield (row, col - 1)
    if row < len(grid) - 1:
        yield (row + 1, col)
    if col < len(grid[0]) - 1:
        yield (row, col + 1)


def perimeter(cell):
    return 4 - sum(
        1 for n in neighbors(cell) if grid[n[0]][n[1]] == grid[cell[0]][cell[1]]
    )


def side_top(cell):
    row, col = cell
    return row == 0 or grid[row - 1][col] != grid[row][col]


def side_bottom(cell):
    row, col = cell
    return row == len(grid) - 1 or grid[row + 1][col] != grid[row][col]


def side_left(cell):
    row, col = cell
    return col == 0 or grid[row][col - 1] != grid[row][col]


def side_right(cell):
    row, col = cell
    return col == len(grid[0]) - 1 or grid[row][col + 1] != grid[row][col]


def sides(cell):
    row, col = cell
    result = 0
    if side_top(cell) and (side_left(cell) or not side_top((row, col - 1))):
        result += 1
    if side_bottom(cell) and (side_left(cell) or not side_bottom((row, col - 1))):
        result += 1
    if side_left(cell) and (side_top(cell) or not side_left((row - 1, col))):
        result += 1
    if side_right(cell) and (side_top(cell) or not side_right((row - 1, col))):
        result += 1
    return result


def dfs(cell, cells, fn):
    cells.remove(cell)
    area_sum = 1
    price_sum = fn(cell)
    for n in neighbors(cell):
        if n in cells and grid[n[0]][n[1]] == grid[cell[0]][cell[1]]:
            a, p = dfs(n, cells, fn)
            area_sum += a
            price_sum += p
    return area_sum, price_sum


def calculate(fn):
    cells = set((row, col) for row in range(len(grid)) for col in range(len(grid[0])))
    price = 0
    while cells:
        cell = next(iter(cells))
        a, p = dfs(cell, cells, fn)
        price += a * p
    return price


print(calculate(perimeter))
print(calculate(sides))
