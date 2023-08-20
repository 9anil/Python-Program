'''Rearrange the Array
You are given a sorted array of positive integers. Ravi is bored with sorted arrays and wants you to rearrange the array.
The new arrangement follows an interesting pattern.In the new pattern, array elements have to be arranged alternatively
i.e. first element should be the maximum value present in the array, the second element should be the minimum value,
the third element should be the second maximum, forth the second minimum and so. Can you write a program to rearrange
the array in the new pattern?
Input format
First-line contains integer T, denoting the number of test cases.For each test case:
First-line contains an integer N.Second line contains N space separated integers Ai.
Output format
For each test case on a new line, print the newly arranged array.'''
T=int(input())
while T>0:
    N=int(input())
    arr=list(map(int,input().split()))
    max=N-1
    min=0
    flag=1
    temp=[0]*N
    for i in range(N):
        if flag==1:
            temp[i]=arr[max]
            print(temp[i],end=" ")
            max-=1
        else:
            temp[i]=arr[min]
            print(temp[i],end=" ")
            min+=1
        flag=1-(flag)
    print()
    T-=1

t=int(input())
while t>0:
  n=int(input())
  arr=list(map(int,input().split()))
  small=0
  large=n-1
  temp=[0]*n
  flag=True
  for i in range(n):
    if flag is True:
      temp[i]=arr[large]
      print(temp[i],end=" ")
      large-=1
    else:
      temp[i]=arr[small]
      print(temp[i],end=" ")
      small+=1
    flag=bool(1-flag)
  # for i in range(n):
  #   arr[i]=temp[i]
  #   print(temp[i])
  print()
  t=t-1