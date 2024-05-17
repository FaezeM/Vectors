def add_row(matrix):
    return [sum(row) for row in matrix]

a = [[1,2,3]]
b = [[1,2,3], [4,5,6], [7,8,9]]
print(add_row(a))
print(add_row(b))