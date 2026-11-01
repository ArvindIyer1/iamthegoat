# Use BFS to solve a planning problem. Examples can be 8 puzzle problems, Robot path
# planning, Blocks world etc.
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


def next_states(state):
    blocked_blocks = {on for block, on in state if on != "Table"}
    result = []

    for block, on in state:
        if block in blocked_blocks:
            continue

        if on != "Table":
            new_state = []
            for b, o in state:
                if b == block:
                    new_state.append((b, "Table"))
                else:
                    new_state.append((b, o))
            result.append((tuple(sorted(new_state)), "Move " + block + " to Table"))

        for target, _ in state:
            if target == block or target in blocked_blocks:
                continue
            new_state = []
            for b, o in state:
                if b == block:
                    new_state.append((b, target))
                else:
                    new_state.append((b, o))
            result.append((tuple(sorted(new_state)), "Move " + block + " onto " + target))

    return result


def bfs(start, goal):
    queue = deque([(start, [])])
    visited = {start}

    while queue:
        state, path = queue.popleft()

        if state == goal:
            return path

        for new_state, action in next_states(state):
            if new_state not in visited:
                visited.add(new_state)
                queue.append((new_state, path + [action]))

    return None


print("Initial State:")
print(initial_state)
print("\nGoal State:")
print(goal_state)

solution = bfs(initial_state, goal_state)

print("\nBFS Solution:")
if solution:
    for step, action in enumerate(solution, 1):
        print(f"Step {step}: {action}")
else:
    print("No solution found.")
