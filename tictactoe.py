def print_board(board):
    """
    Function to print the tic-tac-toe board.
    Args:
        board (list): 2D list representing the game board.
    """
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    """
    Function to check if a player has won the game.
    Args:
        board (list): 2D list representing the game board.
        player (str): Current player ('X' or 'O').
    Returns:
        bool: True if the player has won, False otherwise.
    """
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_board_full(board):
    """
    Function to check if the game board is full (a tie).
    Args:
        board (list): 2D list representing the game board.
    Returns:
        bool: True if the board is full, False otherwise.
    """
    return all(all(cell != ' ' for cell in row) for row in board)

def tic_tac_toe():
    """
    Main function to execute the tic-tac-toe game.
    """
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'

    while True:
        print_board(board)

        row = int(input(f"Player {current_player}, enter row (0, 1, or 2): "))
        col = int(input(f"Player {current_player}, enter column (0, 1, or 2): "))

        if board[row][col] == ' ':
            board[row][col] = current_player
        else:
            print("Cell already taken. Try again.")
            continue

        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break

        if is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break

        current_player = 'O' if current_player == 'X' else 'X'

tic_tac_toe()
