def printSolution(board):
    for i in range(N):
        for j in range(N):
            print(board[i][j], end=" ")
        print()

def isSafe(board, row, col):
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper left diagonal
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check upper right diagonal
    i, j = row, col
    while i >= 0 and j < N:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True

def solveNQueensUtil(board, row):
    if row == N:
        printSolution(board)
        return True

    for col in range(N):
        if isSafe(board, row, col):
            board[row][col] = 1
            if solveNQueensUtil(board, row + 1) == True:
                return True
            board[row][col] = 0

    return False

def solveNQueens():
    board = [[0 for x in range(N)] for y in range(N)]
    if solveNQueensUtil(board, 0) == False:
        print("Solution does not exist")
        return False

# Driver Code
N = 4
solveNQueens()

