# Model-based agent for navigating a grid with obstacles.
grid = [
    ["S", ".", "."],
    ["X", ".", "."],
    [".", ".", "G"]
]

row = 0
col = 0
visited = []
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

while True:
    position = (row, col)
    visited.append(position)
    print("Current position:", position)

    if grid[row][col] == "G":
        print("Goal Reached!")
        break

    moved = False
    for row_change, col_change in directions:
        next_row = row + row_change
        next_col = col + col_change

        inside_grid = (
            0 <= next_row < len(grid)
            and 0 <= next_col < len(grid[0])
        )
        next_position = (next_row, next_col)

        if (
            inside_grid
            and grid[next_row][next_col] != "X"
            and next_position not in visited
        ):
            row, col = next_row, next_col
            moved = True
            break

    if not moved:
        print("No path found!")
        break

print("Visited cells:", visited)
