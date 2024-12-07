from pathlib import Path

input = (Path(__file__).parent / "input.txt").read_text().strip()
grid = input.split("\n")
start_position = next(
    (row, col)
    for row, cells in enumerate(grid)
    for col, cell in enumerate(cells)
    if cell == "^"
)
start_direction = (-1, 0)

position = start_position
direction = start_direction
visited = {position}
while True:
    row, col = position
    row += direction[0]
    col += direction[1]
    if not (0 <= row < len(grid) and 0 <= col < len(grid[row])):
        break
    cell = grid[row][col]
    if cell == "#":
        direction = (direction[1], -direction[0])
        continue
    position = (row, col)
    visited.add(position)
print(len(visited))
