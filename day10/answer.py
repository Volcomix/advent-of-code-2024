from pathlib import Path

input = (Path(__file__).parent / "input.txt").read_text().strip()
grid = [list(map(int, line)) for line in input.split("\n")]

roots = [
    (row, col)
    for row, cells in enumerate(grid)
    for col, cell in enumerate(cells)
    if cell == 0
]


def neighbors(node: tuple[int, int]):
    row, col = node
    coords = [
        (row - 1, col),
        (row + 1, col),
        (row, col - 1),
        (row, col + 1),
    ]
    return [
        (r, c)
        for r, c in coords
        if 0 <= r < len(grid)
        and 0 <= c < len(grid[r])
        and grid[r][c] - grid[row][col] == 1
    ]


def search(node: tuple[int, int], visited: set[tuple[int, int]]):
    if grid[node[0]][node[1]] == 9:
        if node in visited:
            return 0
        visited.add(node)
        return 1
    count = 0
    for neighbor in neighbors(node):
        count += search(neighbor, visited)
    return count


print(sum(search(root, set()) for root in roots))


def search2(node: tuple[int, int]):
    if grid[node[0]][node[1]] == 9:
        return 1
    count = 0
    for neighbor in neighbors(node):
        count += search2(neighbor)
    return count


print(sum(map(search2, roots)))
