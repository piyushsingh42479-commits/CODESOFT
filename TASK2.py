import math
# function to print the board 
def display_board(board):
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 5)
    print("\n")
    
def evaluate_result(board):
    # Check for rows and columns
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return board[0][i]
    # Check for diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]
    # Checking if board is full
    if all(cell != " " for row in board for cell in row):
        return "Draw"
    return None
def minimax_algo(board, depth, maximizing):
    result = evaluate_result(board)
    # Assigning scores for terminal states
    if result == "O":   # AI wins
        return 1 - depth
    elif result == "X": # Human wins
        return depth - 1
    elif result == "Draw":
        return 0
    if maximizing:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"  # AI's move
                    score = minimax_algo(board, depth + 1, False)
                    board[i][j] = " "
                    best_score = max(best_score, score)
        return best_score
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"  # Human's move
                    score = minimax_algo(board, depth + 1, True)
                    board[i][j] = " "
                    best_score = min(best_score, score)
        return best_score
    
def best_move(board):
    best_score = -math.inf
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"
                score = minimax_algo(board, 0, False)
                board[i][j] = " "
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move

def start_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic-Tac-Toe!")
    print("You are X, AI is O.")
    print("Let's start the game.\n")
    display_board(board)
    while True:
        # Human move
        try:
            row = int(input("Enter the row (0-2): "))
            col = int(input("Enter the column (0-2): "))
        except ValueError:
            print("Invalid input Enter the numbers 0,1,or 2.")
            continue
        if row not in range(3) or col not in range(3) or board[row][col] != " ":
            print("Invalid move Please Try again.")
            continue
        board[row][col] = "X"
        display_board(board)
        if evaluate_result(board) is not None:
            break
        # AI move
        AI = best_move(board)
        if AI:
            board[AI[0]][AI[1]] = "O"
            print("AI played its move:")
            display_board(board)
        if evaluate_result(board) is not None:
            break
    # Game over
    result = evaluate_result(board)
    if result == "Draw":
        print("It's a Draw!")
    else:
        print(f"{result} wins the game!")
if __name__ =="__main__":
    start_game()



    
