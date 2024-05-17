def column_addition(matrix):
    sums = [0] * len(matrix[0])
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            sums[j] += matrix[i][j]
    
    return sums

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

print(column_addition(matrix))