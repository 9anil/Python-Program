# T=int(input())
# while 1<=T<=5:
#     arr1=[]
#     min=10000000
#     max=-1
#     for i in input().split():
#         arr1.append(int(i))
#     for j in range(len(arr1)):
#         if(arr1[j]<min):
#             min=arr1[j]
#         elif(arr1[j]>max):
#             max=arr1[j]
#     print("min=",min,"| Max=",max)
#     T=T-1
# a=[1,2,3]
# b=a.copy()
# print(b is a)
# s="dfa@b@c@ad"
# a=list(s.partition("@"))
# print(a)
# b=list(s.split("@",3))
# print(b)

T=int(input())
# while T>0:
#   N=int(input())
#   if (1<=N<=9):
#     A=[]
#     M=1
#     for i in input().split():
#       A.append(int(i))
#     for j in range(len(A)):
#       if(1<=A[j]<=10):
#         M=M*A[j]
#       else:
#         print("Enter valid Number")
#     print(M)
#   T=T-1
T=int(input())
while(T>0):
  N=int(input())
  A=list(map(int,input().split()))
  min=10000001
  max=0
  for i in range(N):
    if (A[i]<min):
      min=A[i]
    if(A[i]>max):
      max=A[i]
  print(min,max)
  T=T-1