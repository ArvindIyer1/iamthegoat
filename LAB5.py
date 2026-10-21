
from collections import deque

initial_state = (
    ("A", "Table"),
    ("B", "Table"),
    ("C", "Table")
)

goal_state = (
    ("A", "B"),
    ("B", "C"),
    ("C", "Table")
)

def get_moves(state):
    moves = []

    # Find blocks that have another block on them
    blocked = {pos for block, pos in state if pos != "Table"}

    for block, pos in state:
        if block in blocked:
            continue

        # Move block to the table
        if pos != "Table":
            new_state = list(state)

            for i, (b, p) in enumerate(new_state):
                if b == block:
                    new_state[i] = (b, "Table")

            moves.append(tuple(new_state))

        # Move block onto another clear block
        for dest, _ in state:
            if dest != block and dest not in blocked and pos != dest:
                new_state = list(state)

                for i, (b, p) in enumerate(new_state):
                    if b == block:
                        new_state[i] = (b, dest)

                moves.append(tuple(new_state))

    return moves

def bfs(start, goal):
    queue = deque([(start, [start])])
    visited = {start}

    while queue:
        state, path = queue.popleft()

        if state == goal:
            return path

        for next_state in get_moves(state):
            if next_state not in visited:
                visited.add(next_state)
                queue.append((next_state, path + [next_state]))

    return None

solution = bfs(initial_state, goal_state)

if solution:
    print("Solution found!")

    for i, state in enumerate(solution):
        print("Step:", i)
        print(state)
        print()
else:
    print("No solution found")
