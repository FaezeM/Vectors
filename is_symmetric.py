def is_symmetric(matrix):
    if len(matrix) == len(matrix[0]):
        for i in matrix:
            for j in range(len(matrix[i])):
                if matrix[i][j] != matrix[j][i]:
                    return False
        return True
    else:
        return False



