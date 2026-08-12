def block_correct(sudoku: list, row_no: int, column_no: int):

    block_size = 3
    start_row = (row_no // block_size) * block_size
    start_col = (column_no // block_size) * block_size

    seen_numbers = set()

    for i in range(start_row, start_row + block_size):
        for j in range(start_col, start_col + block_size):
            num = sudoku[i][j]

            if num != 0:
                if num in seen_numbers:
                    return False
                seen_numbers.add(num)

    return True