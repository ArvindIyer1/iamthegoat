# A* search for the 8-puzzle problem.
goal = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]]

moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def heuristic(state):
    """Count tiles that are not in their goal positions."""
    count = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0 and state[i][j] != goal[i][j]:
                count += 1
    return count


def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j


def to_tuple(state):
    return tuple(tuple(row) for row in state)


def display(state):
    for row in state:
        print(row)
    print()


def astar(start):
    start_key = to_tuple(start)
    open_list = [start_key]
    cost = {start_key: 0}
    parent = {start_key: None}

    while open_list:
        key = min(open_list, key=lambda state: cost[state] + heuristic(state))
        open_list.remove(key)
        current = [list(row) for row in key]

        if current == goal:
            path = []
            while key is not None:
                path.append(key)
                key = parent[key]
            path.reverse()
            return path

        x, y = find_blank(current)
        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 3 and 0 <= ny < 3:
                next_state = [row[:] for row in current]
                next_state[x][y], next_state[nx][ny] = next_state[nx][ny], next_state[x][y]
                next_key = to_tuple(next_state)
                new_cost = cost[key] + 1
                if next_key not in cost or new_cost < cost[next_key]:
                    cost[next_key] = new_cost
                    parent[next_key] = key
                    if next_key not in open_list:
                        open_list.append(next_key)

    return None


start = [[1, 2, 3],
         [4, 0, 6],
         [7, 5, 8]]

path = astar(start)

if path is None:
    print("No solution")
else:
    print("Steps:", len(path) - 1)
    for step, state in enumerate(path):
        print("Step", step)
        display([list(row) for row in state])
