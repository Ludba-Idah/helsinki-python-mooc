def copy_and_add(sudoku: list, row_no: int, column_no: int, number: int):

    new_grid = []
    
    for row in sudoku:
        new_grid.append(list(row))
    
    new_grid[row_no][column_no] = number
    return new_grid
