# print("<------------ Basic approach right rotation-------------------->")
# t=int(input())
# while t>0:
#     n,k=map(int,input().split())
#     arr=list(map(int,input().split()))
#     for i in range(k):
#         temp=arr[n-1]
#         for j in range(n-1,0,-1):
#             arr[j]=arr[j-1]
#         arr[0]=temp
#     for p in range(n):
#         print(arr[p],end=" ")
#     print()
#     t-=1
# print("<------------ Basic approach left rotation-------------------->")
# T=int(input())
# while T>0:
#     N,K=map(int,input().split())
#     arr=list(map(int,input().split()))
#     for i in range(K):
#         temp=arr[0]
#         for j in range(0,N-1):
#             arr[j]=arr[j+1]
#         arr[N-1]=temp
#     for i in range(N):
#         print(arr[i],end=' ')
#     print()
#     T-=1
# def right_rotation(arr,n):
#     temp=arr[n-100]
#     for i in range(n-1,0,-1):
#         arr[i]=arr[i-1]
#     arr[0]=temp
# def printRightRotation(arr,n):
#     print("<------------ Basic approach right rotation by function-------------------->")
#     for i in range(n):
#         print(arr[i],end=" ")
#     print()
# def left_rotation(arr,n):
#     temp=arr[0]
#     for i in range(0,n-1):
#         arr[i]=arr[i+1]
#     arr[n-1]=temp
# def printLeftRotation(arr,n):
#     print("<------------ Basic approach left rotation by function-------------------->")
#     for i in range(n):
#         print(arr[i],end=" ")
#     print()
# def main():
#     t=int(input())
#     while t>0:
#         n,k=map(int,input().split())
#         arr=list(map(int,input().split()))
#         for i in range(k):
#             #right_rotation(arr,n)
#             left_rotation(arr,n)
#         printRightRotation(arr,n)
#         printLeftRotation(arr,n)
#     t-=1
# if __name__=='__main__':
#     main()
# print("<--------------------Optimize approach for right rotation-------------------------->")
# def reversalRightRotation(arr,i,j):
#     while i<j:
#         temp=arr[i]
#         arr[i]=arr[j]
#         arr[j]=temp
#         i+=1
#         j-=1
# def printRightRotation(arr,n):
#     for i in range(n):
#         print(arr[i],end=" ")
#     print()
# def main():
#     t=int(input())
#     while t>0:
#         n,k=map(int,input().split())
#         arr=[int(ele) for ele in input().split()][0:n]
#         reversalRightRotation(arr,n-k,n-1)
#         reversalRightRotation(arr,0,n-k-1)
#         reversalRightRotation(arr,0,n-1)
#         printRightRotation(arr,n)
#         t-=1
# if __name__=='__main__':
#     main()
# print("<--------------------Optimize approach for left rotation-------------------------->")
# def reversalLeftRotation(arr,i,j):
#     while i<j:
#         temp=arr[i]
#         arr[i]=arr[j]
#         arr[j]=temp
#         i+=1
#         j-=1
# def printLeftRotation(arr,n):
#     for i in range(n):
#         print(arr[i],end=" ")
#     print()
# def main():
#     t=int(input())
#     while t>0:
#         n,k=map(int,input().split())
#         arr=[int(ele) for ele in input().split()][0:n]
#         reversalLeftRotation(arr,0,k-1)
#         reversalLeftRotation(arr,k,n-1)
#         reversalLeftRotation(arr,0,n-1)
#         printLeftRotation(arr,n)
#         t-=1
# if __name__=='__main__':
#     main()

def reversalRightRotation(arr,i,j):
  while i<j:
    temp=arr[i]
    arr[i]=arr[j]
    arr[j]=temp
    i+=1
    j-=1
def printRightRotation(arr,n):
  for i in range(n):
    print(arr[i],end=" ")
  print()
def main():
  t=int(input())
  while t>0:
    n,k=map(int,input().split())
    arr=list(map(int,input().split()))
    if k>n:
      k=k%n
    reversalRightRotation(arr,n-k,n-1)
    reversalRightRotation(arr,0,n-k-1)
    reversalRightRotation(arr,0,n-1)
    printRightRotation(arr,n)
    t-=1
if __name__=='__main__':
  main()