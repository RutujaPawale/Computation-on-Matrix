def addMatrices():
    print("Addition of two matrix is:")
    for i in range(rows):
        for j in range(columns):
            result[i][j]=matrix1[i][j] + matrix2[i][j]
            print(" ", result[i][j], end=" ")
        print()
    repeat()

def subMatrices():
    print("Subtraction of two matrix is:")
    for i in range(rows):
        for j in range(columns):
            result[i][j] = matrix1[i][j] - matrix2[i][j]
            print(" ", result[i][j], end=" ")
        print()
    repeat()

def mulMatrices():
    print("Multiplication of two matrix is:")
    for i in range(rows):
        for j in range(columns):
            #for k in range(columns):
            result[i][j] += matrix1[i][j] * matrix2[i][j]
            print(" ", result[i][j], end=" ")
        print()
    repeat()

def transMatrices():
    result=[[0 for i in range(rows)] for j in range(columns)]
    print("Transpose Matrix:")
    for i in range(rows):
        for j in range(columns):
            result[j][i] = matrix1[i][j]
            print(" ", result[i][j], end=" ")
        print()
    repeat()
