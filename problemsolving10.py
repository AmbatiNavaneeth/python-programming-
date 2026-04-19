Check if a Matrix is Square
l=[[1, 2], [3, 4]]
if len(l)!=2:
    print(False)
else:
    for i in l:
        if len(i)!=2:
            print(False)
            break
    else:
        print(True)
        
Print Diagonal Elements
mat=[[1, 2], [3, 4]]
n=len(mat)
res=[]  
for i in range(n):
    res.append(mat[i][i])
print(res) #[[1,4]

Print Anti-Diagonal
mat=[[1, 2], [3, 4]]
n=len(mat)
res=[]
for i in range(n):
    res.append(mat[i][n-i-1])
print(res)  #[2,3]

Printing Non diagonal elements
matrix = [[1, 2,5],
          [3, 4,7],
         [1,2,3]]
n = len(matrix)
res = []
for i in range(n):
    for j in range(n):
        if i != j:
            res.append(matrix[i][j])
print(res) #[2,5,3,7,1,2]
