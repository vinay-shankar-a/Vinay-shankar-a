r=int(input("enter the row size:"))
c=int(input("enter the column size:"))
if (r==c):
    mat=[]
    print("Enter matrix elements:")
    for i in range(r):
        row=[]
        for j in range(c):
            row.append(int(input("enter row element: ")))
        mat.append(row)
    trace=0
    print("Matrix:")
    for i in range(r):
        for j in range(c):
            if i==j:
                trace+=mat[i][j]
            print(mat[i][j],end=" ")
        print()
    print("Trace of the matrix is %d"%trace)