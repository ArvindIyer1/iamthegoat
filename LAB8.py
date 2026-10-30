import math

board = [" "] * 9


def print_board():
    print()
    for i in range(3):
        print(" " + board[i * 3] + " | " + board[i * 3 + 1] + " | " + board[i * 3 + 2])
        if i < 2:
            print("---|---|---")
    print()


def check_winner(player):
    lines = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    for line in lines:
        if all(board[i] == player for i in line):
            return True
    return False


def is_draw():
    return " " not in board


def minimax(is_max):
    if check_winner("O"):
        return 1
    if check_winner("X"):
        return -1
    if is_draw():
        return 0

    if is_max:
        best = -math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(False)
                board[i] = " "
                best = max(best, score)
        return best
    else:
        best = math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(True)
                board[i] = " "
                best = min(best, score)
        return best


def ai_move():
    best_score = -math.inf
    best_move = -1
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(False)
            board[i] = " "
            if score > best_score:
                best_score = score
                best_move = i
    board[best_move] = "O"


def human_move():
    while True:
        try:
            pos = int(input("Enter position (1-9): ")) - 1
            if 0 <= pos < 9 and board[pos] == " ":
                board[pos] = "X"
                break
            print("Invalid move. Try again.")
        except ValueError:
            print("Enter a valid number.")


print("Positions are:")
print("1 | 2 | 3")
print("--|---|--")
print("4 | 5 | 6")
print("--|---|--")
print("7 | 8 | 9")

while True:
    print_board()
    human_move()
    if check_winner("X"):
        print_board()
        print("You Win!")
        break
    if is_draw():
        print_board()
        print("It's a Draw!")
        break
    ai_move()
    if check_winner("O"):
        print_board()
        print("AI Wins!")
        break
    if is_draw():
        print_board()
        print("It's a Draw!")
        break
