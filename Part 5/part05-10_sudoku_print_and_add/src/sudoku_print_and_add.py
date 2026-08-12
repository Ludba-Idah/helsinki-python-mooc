def print_sudoku(sudoku: list):

    for row_no in range(9):

        if row_no > 0 and row_no % 3 == 0:
            print()
            
        for col_no in range(9):

            if col_no > 0 and col_no % 3 == 0:
                print(" ", end="")
                
            value = sudoku[row_no][col_no]
            
            if value == 0:
                print("_ ", end="")
                
            else:
                print(f"{value} ", end="")
        print()

def add_number(sudoku: list, row_no: int, column_no: int, number: int):
    sudoku[row_no][column_no] = number