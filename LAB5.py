from collections import deque
initial_state = (
        ("A","Table"),
        ("B","Table"),
        ("C","Table"),

        ) 

final_state = (
        ("A","B"),
        ("B","C"),
        ("C","Table"),

        ) 

def get_mv(state):
    moves =[]

    blocked = {x for x,y in state if y != "Table"}

    for block,position in state:
        if block in blocked:
            continue

        if position != "Table" :
            new_list = list(state)

            for i,(b,p) in enumerate(new_list):
                if b == block:
                    new_list[i] = (b,"Table")

            moves.append(tuple(new_list))

        for dest, _ in state:
            if dest == block:
                continue
            
            if dest in blocked :
                continue

            if position == dest :
                continue

            new_list = list(state)

            for i,(b,p) in enumerate(new_list):
                if b == block:
                    new_list[i] = (b,dest)

            moves.append(tuple(new_list))

    return moves


def bfs(ini,goal):
    queue = deque([(ini,[])])
    visited = {ini}

    while queue:
        state,path = queue.popleft()

        if state == goal:
            return path + [state]

        for nxt_state in get_mv(state):
            if nxt_state not in visited:
                visited.add(nxt_state)
                queue.append((nxt_state,path +[state]))

    return None

solution = bfs(initial_state, final_state)

if solution:
    print("solution found")

    for i, state in enumerate(solution):
        print(f"Step:{i}")
        print(state)
        print()

else :
    print("No solution Found")

