r=int(input("Enter row size: "))
c=int(input("Enter column size: "))
mat=[]

for i in range (r):
    row=[]
    for j in range (c):
        row.append(int(input("Elements of row:")))
    mat.append(row)

print("Diagonal Matrix:")

for i in range (r):
    for j in range (c):
        print(mat[i][j],end=" ")
        
        
    print()

print("Digonal elements: ")

for i in range (r):
    for j in range (c):
        if(i==j):
            print(mat[i][j],end=" ")