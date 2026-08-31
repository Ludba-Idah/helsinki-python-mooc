def read_matrix():
    matrix = []
    with open("matrix.txt") as file:
        for line in file:
            line = line.strip()
            if line != "":
                parts = line.split(",")
                row = []
                for item in parts:
                    row.append(int(item))
                matrix.append(row)
    return matrix

def matrix_sum():
    matrix = read_matrix()
    total = 0
    for row in matrix:
        for item in row:
            total += item
    return total

def matrix_max():
    matrix = read_matrix()
    maximum = matrix[0][0]
    for row in matrix:
        for item in row:
            if item > maximum:
                maximum = item
    return maximum

def row_sums():
    matrix = read_matrix()
    results = []
    for row in matrix:
        row_sum = 0
        for item in row:
            row_sum += item
        results.append(row_sum)
    return results
