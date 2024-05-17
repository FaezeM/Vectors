def product_mv(matrix , vector):
    result = []
    for row in matrix:
        row_result = sum(row[i] * vector[i] for i in range(len(vector)))
        result.append(row_result)

    return result

def product_matrices(matrix1, matrix2):
    result = [[0 for col in range(len(matrix2[0]))] for row in range(len(matrix1))]

    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix1[0])):
                result[i][j] += matrix1[i][k] * matrix2[k][j]

    return result

a = [[ 1, 2],
[ 3, 4],
[ 5 ,6]]

b = [[ 1, 2],
[ 3, 4]]

c = [[ 1, 2 ,3],
[ 4, 5 ,6],
[ 7, 8 ,9]]

d = [1, 2, 3]

print(product_mv(c, d))
print(product_matrices(a, b))