N = 8

def print_solution(board):
    for row in board:
        print(" ".join("Q" if cell else "." for cell in row))
    print()

def is_safe(board, row, col):
    for previous_row in range(row):
        if board[previous_row][col]:
            return False
        distance = row - previous_row
        left_col = col - distance
        right_col = col + distance
        if left_col >= 0 and board[previous_row][left_col]:
            return False
        if right_col < N and board[previous_row][right_col]:
            return False
    return True

def solve_n_queens(board, row=0):
    if row == N:
        print_solution(board)
        return True
    found = False
    for col in range(N):
        if is_safe(board, row, col):
            board[row][col] = 1
            found = solve_n_queens(board, row + 1) or found
            board[row][col] = 0
    return found

if __name__ == "__main__":
    board = [[0] * N for _ in range(N)]
    print("Solutions to the 8 Queens problem:")
    solve_n_queens(board)
