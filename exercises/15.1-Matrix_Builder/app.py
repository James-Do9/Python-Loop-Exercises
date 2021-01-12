import random

#Create the function below:
def matrixBuilder(num):
    matrix = []
    for i in range(0, num):
        row = []
        for j in range(0, num):
            row.append(random.randint(1,1))
        matrix.append(row)
    return matrix

print(matrixBuilder(3))