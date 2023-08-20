N,M=map(int,input().split())
mat1=[]
mat2=[]
mat3=[]
for i in range(N):
    mat1.append(list(map(int,input().split())))
for i in range(N):
    mat2.append(list(map(int,input().split())))
for i in range(N):
    mat3.append([0]*M)
for i in range(N):
    for j in range(M):
        mat3[i][j]=mat1[i][j]+mat2[i][j]
for i in range(N):
    for j in range(M):
        print(mat3[i][j],end=" ")
    print()


