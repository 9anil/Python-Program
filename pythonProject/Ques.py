n,m=map(int,input().split())
mat1=[]

for i in range(n):
    mat1.append(list(map(int,input().split())))
#ans[3][3]={1}
for i in range(0,n):
    for j in range(0,m):
        if mat1[i][j]%2==1:
            mat1[i][j]=1-mat1[i][j]
            if(i-1>0):
                mat1[i-1][j]=1-mat1[i-1][j]
            if (i+1<=2):
                mat1[i+1][j]=1-mat1[i+1][j]
            if(j-1>=0):
                mat1[i][j-1]=1-mat1[i][j-1]
            if(j+1<=2):
                mat1[i][j+1]=1-mat1[i][j+1]
for i in range(0,2):
    for j in range(0,2):
        print(mat1[i][j])

