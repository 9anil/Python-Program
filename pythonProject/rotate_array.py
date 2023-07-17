# def rightRotate(arr,n):
#     temp=arr[n-1]
#     for i in range(n-1,0,-1):
#         arr[i]=arr[i-1]
#     arr[0]=temp
# def printArr(arr,n):
#     for i in range(n):
#         print(arr[i],end=" ")
#     print()
# def main():
#     t=int(input())
#     while t>0:
#         n,k=map(int,input().split())
#         arr=list(map(int,input().split()))
#         for i in range(k):
#             rightRotate(arr,n)
#         printArr(arr,n)
#         t=t-1
# if __name__=='__main__':
#     main()
# def rightRotate():
#     t=int(input())
#     while t>0:
#         n,k=map(int,input().split())
#         arr=list(map(int,input().split()))
#         for i in range(k):
#             temp=arr[n-1]
#             for i in range(n-1,0,-1):
#                 arr[i]=arr[i-1]
#                 #print(arr[i])
#             arr[0]=temp
#         for i in range(n):
#             print(arr[i],end=" ")
#         print()
#         t=t-1
# rightRotate()
# t=int(input())
# while t>0:
#   n,k=map(int,input().split())
#   arr=list(map(int,input()).split())
#   for i in range(k):
#     temp=arr[n-1]
#     for j in range(n-1,0,-1):
#       arr[j]=arr[j-1]
#     arr[0]=temp
#   for i in range(n):
#     print(arr[i],end=" ")
#   t=t-1
def rotate(arr,n,k):
  temp=arr[n-1]
  for j in range (n-1,0,-1):
    arr[j]=arr[j-1]
  arr[0]=temp
def print_rotate(arr,n):
  for i in range(n):
    print(arr[i],end=" ")
  print()
def main():
  t=int(input())
  while t>0:
    n,k=map(int,input().split())
    arr=list(map(int,input().split()))
    if (k<=10**4):
      for i in range(k):
        rotate(arr,n,k)
      print_rotate(arr,n)
    else:
      for i in range(k):
        rotate(arr,n,k)
      print_rotate(arr,n)
    t=t-1
if __name__=='__main__':
  main()