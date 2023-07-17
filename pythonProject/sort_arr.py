# sort an array in ascending order
# t=int(input())
# while t > 0:
#     n = int(input())
#     ar = list(map(int, input().split()))
#     for i in range(n):
#         for j in range(i+1, n):
#             if ar[i] > ar[j]:
#                 temp=ar[i]
#                 ar[i] = ar[j]
#                 ar[j]=temp
#         print(ar[i],end=" ")
#     t=t-1
# Reversal algo right rotation implementation
# t=int(input())
# while t>0:
#     n,k=map(int,input().split())
#     arr=list(map(int,input().split()))
#     for i in range(k,n):
#         for j in range(i+1,n):
#             temp=arr[i]
#             arr[i]=arr[j]
#             arr[j]=temp
#         #print(arr[i],end=" ")
#     for i in range(0,k):
#         for j in range(i+1,k):
#             temp=arr[i]
#             arr[i]=arr[j]
#             arr[j]=temp
#        # print(arr[i],end=" ")
#     for i in range(0,n):
#         for j in range(i+1,n):
#             temp=arr[i]
#             arr[i]=arr[j]
#             arr[j]=temp
#         print(arr[i],end=" ")
#     t=t-1
# def Rightreversal_algo(arr,i,j):
#     while i<j:
#         temp=arr[i]
#         arr[i]=arr[j]
#         arr[j]=temp
#         i+=1
#         j-=1
# def printreversal(arr,n):
#      for i in range(n):
#          print(arr[i],end=" ")
#      print()
# def main():
#     t=int(input())
#     while t>0:
#         n,k=map(int,input().split())
#         arr=list(map(int,input().split()))
#         Rightreversal_algo(arr,n-k,n-1)
#         Rightreversal_algo(arr,0,n-k-1)
#         Rightreversal_algo(arr,0,n - 1)
#         printreversal(arr,n)
#         t=t-1
# if __name__=='__main__':
#     main()
# Addition of matrix
# m,n=map(int,input().split())
# mat1=[]
# mat2=[]
# mat3=[]
# for i in range(n):
#     mat1.append(list(map(int,input().split())))
# for i in range(n):
#     mat2.append(list(map(int,input().split())))
# for i in range(n):
#     mat3.append([0]*m)
# for i in range(n):
#     for j in range(m):
#         mat3[i][j]=mat1[i][j]+mat2[i][j]
# for i in range(n):
#     for j in range(m):
#         print(mat3[i][j],end=" ")
#     print()
'''Multiplicaton of two mattrix'''
# m,n=map(int,input().split())
# mat1=[]
# mat2=[]
# mat3=[]
# for i in range(n):
#     mat1.append(list(map(int,input().split())))
# for i in range(n):
#     mat2.append(list(map(int,input().split())))
# for i in range(n):
#     mat3.append([0]*m)
# for i in range(n):
#     for j in range(m):
#         for k in range(m):
#             mat3[i][j]=mat3[i][j]+mat2[i][k]*mat2[k][j]
# for i in range(n):
#     for j in range(m):
#         print(mat3[i][j],end=" ")
#     print()
'''Frequency of array'''
n=int(input())
arr=list(map(int,input().split()))
count=0
for i in range(n):
    for j in range(n):
        if i!=j:
            if arr[i]==arr[j]:
                count=count+1
print(count)
