r1=int(input("Enter number of rows for first matrix: "))
c1=int(input("Enter number of columns for first matrix: "))
r2=int(input("Enter number of rows for second matrix: "))
c2=int(input("Enter number of columns for second matrix: "))
if(r1==r2 and c1==c2):
    mat1=[]
    print("Enter matrix 1:")
    for i in range(r1):
        row=[]
        for j in range(c1):
            row.append(int(input("Enter element: ")))
        mat1.append(row)
    print("Enter matrix 2: ")
    mat2=[]
    for i in range(r2):
        row=[]
        for j in range(c2):
            row.append(int(input("Enter element: ")))
        mat2.append(row)
    print("First matrix is: ")
    for i in range(r1):
        for j in range(c1):
            print(mat1[i][j],end="  ")
        print("\n")
    print("Second matrix is : ")
    for i in range(r1):
        for j in range(c1):
            print(mat2[i][j],end="  ")
        print("\n")
    print("Subtration of two matrix is:")
    for i in range(r1):
        for j in range(c1):
            print(mat1[i][j]-mat2[i][j],end="  ")
        print("\n")
else:
    print("Subtration is not possible.")