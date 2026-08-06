def transpose(matrix: list):

    number = len(matrix)

    for row in range(number):

        for integer in range(row + 1, number):
            
            matrix[row][integer], matrix[integer][row] = matrix[integer][row], matrix[row][integer]

if __name__ == "__main__":

    matrix =  [[1, 2, 3], [4, 5, 6], [7, 8 ,9]]
    transpose(matrix)
    print(matrix)
 