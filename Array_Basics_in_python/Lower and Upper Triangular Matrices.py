'''Lower and Upper Triangular Matrices
You are given an M*N matrix, print lower triangular matrix and upper triangular matrix.See sample test case for
better understanding.
Input format
First line contains M and N representing rows and columns respectively.Each of the next M lines contains N integers.
Output format
Lower Triangular Matrix
Upper Triangular Matrix'''
def upperMatrix(mat,m,n):
    for i in range(m):
        for j in range(n):
            if i<=j:
                print(mat[i][j],end=" ")
            else:
                print(0,end=" ")
        print()
def lowerMatrix(mat,m,n):
    for i in range(m):
        for j in range(n):
            if i>=j:
                print(mat[i][j],end=" ")
            else:
                print(0,end=" ")
        print()
def main():
    m,n=map(int,input().split())
    mat=[]
    for i in range(m):
        mat.append(list(map(int,input().split())))
    lowerMatrix(mat,m,n)
    upperMatrix(mat,m,n)
if __name__=='__main__':
    main()
