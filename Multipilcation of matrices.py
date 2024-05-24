r1=int(input("enter the 1st row size:"))
c1=int(input("enter the 1st column size:"))
r2=int(input("enter the 2nd row size:"))
c2=int(input("enter the 2nd column size:"))
if (r1==c2 and c1==r2):
    mat1=[]
    mat2=[]
    print("Enter matrix1 elements:")
    for i in range(r1):
        row1=[]
        for j in range(c1):
            row1.append(int(input("enter row element: ")))
        mat1.append(row1)
    print("Matrix1:")
    for i in range(r1):
        for j in range(c1):
            print(mat1[i][j],end=" ")
        print()
    print("Enter matrix2 elements")
    for i in range(r2):
        row2=[]
        for j in range(c2):
            row2.append(int(input("enter row element: ")))
        mat2.append(row2)
    print("Matrix2:")
    for i in range(r2):
        for j in range(c2):
            print(mat2[i][j],end=" ")
        print()
    mat=[]

    for i in range(r1):
        row=[]
        for j in range(c2):
            sum=0
            for k in range(c1):
                sum+=mat1[i][k]*mat2[k][j]
            row.append(sum)
        mat.append(row)  
    print("the mul of matrices is")
    for i in range(r1):
        for j in range(c2):
            print(mat[i][j],end=" ")
        print()              
else:
    print("------the mul is not possible------")