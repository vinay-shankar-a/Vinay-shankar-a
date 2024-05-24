# transpose matrix
r = int(input("Enter row size:"))
c = int(input("Enter col size:"))
mat = []
for i in range(r):
    row = []
    for j in range(c):
        row.append(int(input("Enter element:")))
    mat.append(row)
print("Matrix:")
for i in range(r):
    for j in range(c):
        print(" %d"%mat[i][j],end= " ")
    print()

print("Transpose of Matrix:")
for i in range(c):
    for j in range(r):
        print(" %d"%mat[j][i],end= " ")
        print()