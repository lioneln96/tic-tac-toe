def check_winner(board, player):
    for row in board:
        if row[0] == row[1] == row[2] == player:
            return True

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == player:
            return True

    if board[0][0] == board[1][1] == board[2][2] == player or board[0][2] == board[1][1] == board[2][0] == player:
        return True

    return False


def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def tic_tac_toe():
    game_on = True

    board = []
    for _ in range(3):
        row = []
        for _ in range(3):
            row.append(" ")
        board.append(row)

    current_player = "X"

    print("Welcome to Tic Tac Toe!")
    print_board(board)

    while game_on:
        row = int(input(f"Player {current_player}, choose from rows 1-3: ")) - 1
        col = int(input(f"Player {current_player}, choose from columns 1-3: ")) - 1

        if board[row][col] == " ":
            board[row][col] = current_player

        else:
            print("That position is already taken. Try again.")
            continue

        print_board(board)

        if check_winner(board, current_player):
            print(f"Player {current_player} wins!")
            game_on = False

        elif all(cell != " " for row in board for cell in row):
            print("It's a draw!")
            game_on = False

        if current_player == "X":
            current_player = "O"
        else:
            current_player = "X"


tic_tac_toe()
