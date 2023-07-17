# #SUM OF TWO MATTRIX
# n,m=map(int,input().split())
# mat1=[]
# mat2=[]
# mat3=[]
# for i in range(n):
#     mat1.append(list(map(int,input().split())))
# for i in range(n):
#     mat2.append(list(map(int,input().split())))
# for i in range(n):
#     mat3.append([0]*m)
# '''Addition of matrix'''
# # for i in range(n):
# #     for j in range(m):
# #         mat3[i][j]=mat1[i][j]+mat2[i][j]
# '''Multiplication of matrix'''
# for i in range(n):
#     for j in range(m):
#         for k in range(m):
#             mat3[i][j]=mat3[i][j]+mat1[i][k]*mat2[k][j]
# for i in range(n):
#     for j in range(m):
#         print(mat3[i][j],end=" ")
#     print()

def addition(mat1,mat2,mat3,m,n):
  for i in range(m):
    for j in range(n):
      mat3[i][j]=mat1[i][j]+mat2[i][j]
  for i in range(m):
    for j in range(n):
      print(mat3[i][j])
    print()
# def multiplication(mat1,mat2,mat3,m,n):
#   for i in range(m):
#     for j in range(n):
#       for k in range(n):
#         mat3[i][j]=mat3[i][j]+mat1[i][k]*mat2[k][j]
#   for i in range(m):
#     for j in range(n):
#       print(mat3[i][j])
#     print()
# def main():
#   m,n=map(int,input().split())
#   mat1=[]
#   mat2=[]
#   mat3=[]
#   for i in range(m):
#     mat1.append(list(map(int,input().split())))
#   for i in range(m):
#     mat2.append(list(map(int,input().split())))
#   for i in range(m):
#     mat3.append([0]*m)
#   addition(mat1,mat2,mat3,m,n)
#   multiplication(mat1,mat2,mat3,m,n)
# if __name__=='__main__':
#   main()
# m, n = map(int, input().split())
# mat1 = []
# for i in range(2):
#     for j in range(3):
#         mat1.append(list(map(int, input().split())))
#     print()
# for i in range(m):
#     for j in range(n):
#         print(mat1[i][j])
#     print()

def lower_triangular(mat1,m,n):
  for i in range(m):
    for j in range(n):
      if i<j:
        print(0,end=" ")
      else:
        print(mat1[i][j],end=" ")
    print()
def upper_triangular(mat1,m,n):
    for i in range(m):
      for j in range(n):
        if i>j:
          print(0,end=" ")
        else:
          print(mat1[i][j])
      print()
def main():
  m,n=map(int,input().split())
  mat1=[]
  for i in range(m):
    mat1.append(list(map(int,input().split())))
  lower_triangular(mat1,m,n)
  upper_triangular(mat1,m,n)
if __name__=='__main__':
  main()