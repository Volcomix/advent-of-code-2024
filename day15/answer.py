from pathlib import Path


class Grid:
    cells: list[list[str]]
    width: int
    height: int

    def __init__(self, input: str):
        self.cells = list(reversed(list(map(list, input.splitlines()))))
        self.width = len(self.cells[0])
        self.height = len(self.cells)

    def get(self, x: int, y: int):
        return self.cells[y][x]

    def set(self, x: int, y: int, value: str):
        self.cells[y][x] = value

    def find_robot(self):
        return next(
            (x, y)
            for x in range(grid.width)
            for y in range(grid.height)
            if grid.get(x, y) in "@"
        )

    def __str__(self):
        return "\n".join("".join(row) for row in reversed(self.cells))


def parse_moves(input: str):
    return [
        (0, 1) if c == "^" else (1, 0) if c == ">" else (0, -1) if c == "v" else (-1, 0)
        for c in "".join(input.splitlines())
    ]


def parse_input(input: str):
    input_grid, input_moves = input.split("\n\n")
    grid = Grid(input_grid)
    moves = parse_moves(input_moves)
    return grid, moves


def read_input():
    input = (Path(__file__).parent / "input.txt").read_text().strip()
    return parse_input(input)


def move_cell(cell: tuple[int, int], move: tuple[int, int]):
    content = grid.get(*cell)
    if content == "#":
        return False
    if content == ".":
        return True

    if move_cell((cell[0] + move[0], cell[1] + move[1]), move):
        grid.set(cell[0], cell[1], ".")
        grid.set(cell[0] + move[0], cell[1] + move[1], content)
        return True

    return False


grid, moves = read_input()
robot = grid.find_robot()
for move in moves:
    if move_cell(robot, move):
        robot = (robot[0] + move[0], robot[1] + move[1])

print(
    sum(
        100 * (grid.height - 1 - y) + x
        for x in range(grid.width)
        for y in range(grid.height)
        if grid.get(x, y) == "O"
    )
)
