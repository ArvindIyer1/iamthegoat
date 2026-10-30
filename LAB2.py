grid = [
    ["S", ".", "."],
    ["X", ".", "."],
    [".", ".", "G"]
]

moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]

row, col = 0, 0
visited = []

while True:
    visited.append((row, col))
    print("Current position:", (row, col))

    if grid[row][col] == "G":
        print("Goal reached")
        break

    moved = False
    for dr, dc in moves:
        nr, nc = row + dr, col + dc
        if 0 <= nr < 3 and 0 <= nc < 3:
            if grid[nr][nc] != "X" and (nr, nc) not in visited:
                row, col = nr, nc
                moved = True
                break

    if not moved:
        print("No path found")
        break

print("Visited cells:", visited)
