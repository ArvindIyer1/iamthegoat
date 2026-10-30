def print_board(board, n):
    for i in range(n):
        for j in range(n):
            print(board[i][j], end=" ")
        print()
    print()


def is_safe(board, row, col, n):
    for i in range(col):
        if board[row][i] == 1:
            return False

    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    i, j = row, col
    while i < n and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True


def place_queens(board, col, n):
    if col >= n:
        return True

    for row in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            if place_queens(board, col + 1, n):
                return True
            board[row][col] = 0

    return False


def solve(n):
    board = [[0] * n for _ in range(n)]
    if not place_queens(board, 0, n):
        print("No solution for", n, "queens")
        return
    print(n, "Queens Solution:")
    print_board(board, n)


# 4-Queens
solve(4)

# 8-Queens
solve(8)
