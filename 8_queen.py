def initialize_board(n = 8):
    return [-1] * n

def is_safe(board, row, col):
    for i in range(row):
        if board[i] == col or \
        board[i] - i == col - row or \
        board[i] + i == col + row:
            return False
    return True


def solve_n_queens_recursive(board, row, n):

    if row >= n:
        print_solution(board)
        return True

    for col in range(n):

        if is_safe(board, row, col):
            board[row] = col 
            if solve_n_queens_recursive(board, row + 1, n):
                return True  
            
            board[row] = -1

    return False

def print_solution(board):
    n = len(board)
    for row in range(n):
        line = ""
        for col in range(n):
            if board[row] == col:
                line += "Q "
            else:
                line += ". "
        print(line)
    print("\n")

def solve_n_queens(n=8):
    board = [-1] * n
    if not solve_n_queens_recursive(board, 0, n):
        print("No solution exists")
    else:
        print("Solutions found")


solve_n_queens(8)