r=int(input("Enter row size: "))
c=int(input("Enter column size: "))
mat=[ ]
if r==c:
    for i in range (r):
        row=[]
        for j in range (c):
            row.append(int(input("Elements of row:")))
        mat.append(row)
    print("Matrix:")
    for i in range (r):
        for j in range (c):
            print(mat[i][j],end=" ") 
        print()
else:
    print("It is not a square matrix")