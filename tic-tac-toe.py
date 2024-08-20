def print_board(board):
    for row in board:
        print(" ".join(row))

def check_win(board):
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    for col in range(len(board)):
        check = []
        for row in board:
            check.append(row[col])
        if check.count(check[0]) == len(check) and check[0] != " ":
            return True

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True
    return False     

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print_board(board)
    current_player = "X"

    while True:
        print("Player", current_player, "turn")
        move_row = int(input("Enter the row number (0-2)"))
        move_col = int(input("Enter the column number (0-2)"))

        if board[move_row][move_col] == " ":
            board[move_row][move_col] = current_player
            print_board(board)
            if check_win(board):
                print("Player", current_player, "wins!")
                break
            current_player = "O" if current_player == "X" else "X"
        else:
            print("Invalid move, please try again.")

tic_tac_toe()