
def vector_addition():
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

    #add = []
    #for element in range(len(vec)):
        #add.append(vec[element] + vect[element])

    return [i+j for i, j in zip(vec, vect)]

print(vector_addition())