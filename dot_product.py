
def vector_dot_product():
    while True:
        try:

            vec = input("Please enter the vector .eg: 1234:\n")
            vec = list(vec)
            break

        except ValueError: 

            print("Please enter a valid vector")

    while True:
        try:

            vect = input("Please enter the vector .eg: 1234:\n")
            vect = list(vect)
            if len(vec) != len(vect):
                raise ValueError("Unequal vectors")
            break

        except ValueError: 

            print("Please enter a valid vector")

    #sum = 0
    #for index in range(len(vec)):
        #sum += int(vec[index]) * int(vect[index])

    return sum([int(i)*int(j) for i, j in zip(vec, vect)])

print(vector_dot_product())