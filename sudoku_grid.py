def sudoku_grid_correct(sudoku: list):

    for row in sudoku:
        numbers = []
        for num in row:
            if num != 0 and num in numbers:
                return False
            numbers.append(num)

    for col in range(9):
        numbers = []
        for row in range(9):
            num = sudoku[row][col]
            if num != 0 and num in numbers:
                return False
            numbers.append(num)

    for r in (0, 3, 6):
        for c in (0, 3, 6):
            numbers = []
            for i in range(3):
                for j in range(3):
                    num = sudoku[r + i][c + j]
                    if num != 0 and num in numbers:
                        return False
                    numbers.append(num)

    return True