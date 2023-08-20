n,m=map(int,input().split())
mat1=[]
mat2=[]
mat3=[]
for i in range(n):
    mat1.append(list(map(int,input().split())))
for i in range(n):
    mat2.append(list(map(int,input().split())))
for i in range(n):
    mat3.append([0]*m)
for i in range(n):
    for j in range(m):
        for k in range(m):
            mat3[i][j]=mat3[i][j]+(mat1[i][k]*mat2[k][j])
for i in range(n):
    for j in range(m):
        print(mat3[i][j],end=" ")
    print()