'''Scalar Multiplication
You are given a M*N matrix, and a variable K, print the resultant matrix after scalar multiplication.
Input format
First line contains M,N and K representing rows, columns and scalar.Each of the next M lines contains N integers.
Output format
Print the resultant matrix.'''
m,n,k=map(int,input().split())
mat=[]
for i in range(m):
    mat.append(list(map(int,input().split())))
for i in range(n):
    for j in range(m):
        print(mat[i][j]*k,end=" ")
    print()
print("<------------------------------------***------------------------------------------>")
def scalarMul(mat,m,n,k):
    for i in range(m):
        for j in range(n):
            print(mat[i][j]*k,end=" ")
        print()
def main():
    m,n,k=map(int,input().split())
    mat=[]
    for i in range(m):
        mat.append(list(map(int,input().split())))
    scalarMul(mat,m,n,k)
if __name__=='__main__':
    main()