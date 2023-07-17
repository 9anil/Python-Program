# arr=[]
# for element in input().split():
#     arr.append(int(element))
# for i in range(len(arr)):
#     print(arr[i],end=" ")
#
# arr1=list(map(int,input().split()))
# print(arr1)
# for i in arr1:
#     print(i,end=" ")
# print("")
# for j in range(len(arr1)):
#     print(arr1[j],end=" ")
# N=int(input())
# while N>1:
#   A=[]
#   EVEN=[]
#   ODD=[]
#   for i in input().split():
#     A.append(int(i))
#   for i in range(len(A)):
#     if(A[i]%2==0):
#       EVEN.append(A[i])
#     else:
#       ODD.append(A[i])
#   for e in EVEN:
#     print(e,end=" ")
#   print("")
#   for o in ODD:
#     print(o,end=" ")
#   N=N-1
# creating an empty list

# number of elements
# n = int(input("Enter number of elements : "))
#
# # Below line read inputs from user using map() function
# a = list(map(int, input("\nEnter the numbers : ").split()))[:n]
#
# print("\nList is - ", a)
# N=int(input())
# EVEN=[]
# ODD=[]
# ARR=list(map(int,input().split()))[:N]
# for i in ARR:
#    if (N>1 and (i%2==0 or i%2==1)):
#      if(i%2==0):
#        EVEN.append(i)
#      else:
#        ODD.append(i)
#      for e in EVEN:
#          print(e,end=" ")
#      print("")
#      for o in ODD:
#          print(o,end=" ")
#    else:
#        print("Invalid entry!")
T=int(input())
while T>0:
  N=int(input())
  A=list(map(int,input().split()))[:N]
  min=1000
  for i in range(len(A)):
    if(A[i]<min):
      min=A[i]
  print(min)
  for j in range(len(A)):
    A[j]=min
  print(j-1)
  T=T-1