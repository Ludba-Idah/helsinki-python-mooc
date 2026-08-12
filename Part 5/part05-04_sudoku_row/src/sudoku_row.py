def row_correct(sudoku: list, row_no: int):

    list_of_numbers = []
    error_number = 0

    for num in sudoku[row_no]:
        if num == 0:
            continue

        if num in list_of_numbers:
            error_number = num   

        list_of_numbers.append(num)

    if error_number == 0:
        return True
    else:
        return False