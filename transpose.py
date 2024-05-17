a = [[1,2],[3,4],[5,6]]

def transpose(matrix):
    li = []
    for c in range(len(matrix[0])): #range(len(a[0]))
        lis = []
        for i in matrix:
            lis.append(i[c])
        li.append(lis)
        
    return li