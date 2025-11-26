matrix=[[1,2,3],
        [4,5,6],
        [7,8,9]]

print(matrix)

print(len(matrix))

print(len(matrix[0]))

for i in range(0,len(matrix)):
    for j in range(0,len(matrix[0])):
        print(matrix[i][j],end=" ")

rows=int(input("how many rows"))
columns=int(input("how many columns"))

newmatrix=[]
for i in range(rows):
    temp=[]
    for j in range(columns):
        x=int(input("enter number"))
        temp.append(x)
    newmatrix.append(temp)