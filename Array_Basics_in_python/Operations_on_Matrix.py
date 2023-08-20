'''Operations on Matrix
You are given M and N representing the number of rows and columns of matrix respectively. And M*N elements are provided
for each matrix. There are two matrices in the input.Print the Addition and Multiplication of the matrices.
Input format
First line contains two integers M and N On each of the next 2*M lines, N integers are provided.
Output format
Print the matrix representing the addition
Print the matrix representing the multiplication'''
def additionMat(mat1,mat2,m,n):
    for i in range(m):
        for j in range(n):
            print(mat1[i][j]+mat2[i][j],end=" ")
        print()
def multiplicationMat(mat1,mat2,mat3,m,n):
    for i in range(m):
        for j in range(n):
            for k in range(n):
                mat3[i][j]=mat3[i][j]+(mat1[i][k]*mat2[k][j])
def printMultiplication(mat3,m,n):
    for i in range(m):
        for j in range(n):
            print(mat3[i][j],end=" ")
        print()
def main():
    m,n=map(int,input().split())
    mat1=[]
    mat2=[]
    mat3=[]
    for i in range(m):
        mat1.append(list(map(int,input().split())))
    for i in range(m):
        mat2.append(list(map(int,input().split())))
    for i in range(m):
        mat3.append([0]*m)
    additionMat(mat1,mat2,m,n)
    multiplicationMat(mat1,mat2,mat3,m,n)
    printMultiplication(mat3,m,n)
if __name__=='__main__':
    main()