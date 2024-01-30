def print_board(board):
    # Function to print the current state of the board
    for row in board:
        print(" ".join(map(str, row)))
    print()

def find_blank(board):
    # Function to find the position of the blank space (0) on the board
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                return i, j

def is_valid_move(i, j):
    # Function to check if a move is within the boundaries of the board
    return 0 <= i < 3 and 0 <= j < 3

def apply_move(board, move):
    # Function to apply the specified move to the board
    i, j = find_blank(board)
    new_i, new_j = i + move[0], j + move[1]
    board[i][j], board[new_i][new_j] = board[new_i][new_j], board[i][j]

def is_goal(board):
    # Function to check if the board is in the goal state
    return board == [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

def solve_puzzle(initial_board):
    # List of possible moves: right, down, left, up
    moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    current_board = initial_board.copy()

    # Main loop until the goal state is reached
    while not is_goal(current_board):
        print_board(current_board)
        blank_i, blank_j = find_blank(current_board)

        print("Possible moves:")
        # Display possible moves for the user
        for move in moves:
            new_i, new_j = blank_i + move[0], blank_j + move[1]
            if is_valid_move(new_i, new_j):
                print(move, end=' ')
        print()

        # Get user input for the next move
        user_input = input("Enter your move (e.g., '0 1' to move the blank space to the right): ")
        move = tuple(map(int, user_input.split()))

        # Check if the user's move is valid and apply it
        if move in moves and is_valid_move(blank_i + move[0], blank_j + move[1]):
            apply_move(current_board, move)
        else:
            print("Invalid move. Try again.")

    print("Puzzle solved!")
    print_board(current_board)

# Example usage:
initial_board = [[1, 2, 3], [4, 5, 6], [0, 7, 8]]
solve_puzzle(initial_board)
