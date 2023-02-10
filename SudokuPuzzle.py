def solve_sudoku(grid):
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                for num in range(1,10):
                    if is_valid(grid, row, col, num):
                        grid[row][col] = num
                        if solve_sudoku(grid):
                            return True

                        grid[row][col] = 0
                return False
    return True

def is_valid(grid, row, col, num):
    # Check the current row
    for i in range(9):
        if grid[row][i] == num or grid[i][col] == num:
            return False

    # Check the current 3x3 box
    row_start = (row//3)*3
    col_start = (col//3)*3
    for i in range(3):
        for j in range(3):
            if grid[row_start+i][col_start+j] == num:
                return False
    # If the number is not found in the current row, column, or box, return True
    return True

grid = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

# Check if a solution exists
if solve_sudoku(grid):
    # Print the solution
    for row in grid:
        print(row)
else:
    # If no solution exists, print a message
    print("No solution exists")
 
