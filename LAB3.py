start = [[1,2,3],[4,0,6],[7,5,8]]
goal = [[1,2,3],[4,5,6],[7,8,0]]



def heuristic(state):
    h = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0 and state[i][j] != goal[i][j]:
                h+=1
    return h
                


def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i,j


def copy_state(state):
    return [row[:] for row in state]

def neighbors(state):
    x,y = find_blank(state)
    moves = [(-1,0),(1,0),(0,-1),(0,1)]
    result = []
    for dx,dy in moves:
        nx,ny = x+ dx,y+dy
        if 0 <= nx <3 and 0<=ny<=3:
            new_state = copy_state(state)
            new_state[x][y],new_state[nx][ny] = new_state[nx][ny],new_state[x][y]
            result.append(new_state)

    return result

def astar(state):
    open_list = [(start,0)]
    visited = []

    while open_list:
        best = 0
        for i in range (1,len(open_list)):
            s,g = open_list[i]
            bs,bg = open_list[best]
            if g + heuristic(s) < bg + heuristic(bs):
                best = i
        state,g = open_list.pop(best)
        print("Current State:")
        for row in state:
            print(row)
        print("g =",g)
        print("h = ",heuristic(state))
        print("f=", g + heuristic(state))
        print()

        if state == goal:
            print("Goal found :")
            return

        visited.append(state)

        for nxt in neighbors(state):
            if nxt not in visited:
                open_list.append((nxt,g+1))

    print("No solution")

astar(start)