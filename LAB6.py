N = 4

def printSolution(board):
    for row in board:
        print(*row)

def isSafe(board, row, col):
    # Check left side of row
    for j in range(col):
        if board[row][j] == 1:
            return False

    # Check upper diagonal
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check lower diagonal
    i, j = row, col
    while i < N and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True

def solve(board, col):
    if col >= N:
        return True

    for row in range(N):
        if isSafe(board, row, col):
            board[row][col] = 1

            if solve(board, col + 1):
                return True

            board[row][col] = 0

    return False

board = [[0] * N for _ in range(N)]

if solve(board, 0):
    print("Solution:")
    printSolution(board)
else:
    print("Solution does not exist")



# //8 queens problem

N = 8

def printSolution(board):
    for row in board:
        print(*row)

def isSafe(board, row, col):
    # Check left side of row
    for j in range(col):
        if board[row][j] == 1:
            return False

    # Check upper diagonal
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check lower diagonal
    i, j = row, col
    while i < N and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True

def solve(board, col):
    if col >= N:
        return True

    for row in range(N):
        if isSafe(board, row, col):
            board[row][col] = 1

            if solve(board, col + 1):
                return True

            board[row][col] = 0

    return False

board = [[0] * N for _ in range(N)]

if solve(board, 0):
    print("Solution:")
    printSolution(board)
else:
    print("Solution does not exist")