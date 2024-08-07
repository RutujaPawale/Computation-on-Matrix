def addMatrices():
    print("Addition of two matrix is:")
    for i in range(rows):
        for j in range(columns):
            result[i][j]=matrix1[i][j] + matrix2[i][j]
            print(" ", result[i][j], end=" ")
        print()
    repeat()
