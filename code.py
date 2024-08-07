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

rows = int(input("Enter number of rows:"))
columns = int(input("Enter number of columns:"))

matrix1= [[0 for i in range(rows)] for j in range(columns)]
matrix2 = [[0 for i in range(rows)] for j in range(columns)]
result = [[0 for i in range(rows)] for j in range(columns)]

print("Enter first Matrix:")
for i in range(rows):
    a = []
    for j in range(columns):
        a.append(int(input()))
    matrix1.append(a)
print("Enter second Matrix:")
for i in range(rows):
    b = []
    for j in range(columns):
        b.append(int(input()))
    matrix2.append(b)

for i in range(rows):
    for j in range(columns):
        print(matrix1[i][j], end=" ")
    print()
for i in range(rows):
    for j in range(columns):
        print(matrix1[i][j], end=" ")
    print()
