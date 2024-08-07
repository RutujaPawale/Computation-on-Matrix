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

def repeat():
    num = int(input("Which operation do you want to perform:"))
    str(num).strip()

    if num == 1:
        addMatrices()
    elif num == 2:
        subMatrices()
    elif num == 3:
        mulMatrices()
    elif num == 4:
        transMatrices()
    elif num==5:
        print("Thank you !!")
        exit()
    else:
        print("Invalid Input!")
