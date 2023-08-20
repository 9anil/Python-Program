'''Array Zigzag
You are given an array of N integers. You have to make the given array into a zigzag array. During converting given
array into a zigzag array you can perform a move, which consists of choosing any element and decreasing it by 1.
An array A is a zigzag array if either:
1. Every even-indexed element is greater than adjacent elements, ie. A[0]>A[1]<A[2]>A[3]<A[4]>...
2. OR, every odd-indexed element is greater than adjacent elements, ie. A[0]<A[1]>A[2]<A[3]>A[4]<...
Print the minimum number of moves to transform the given array into a zigzag array.
Input Format
The first line contains an integer N size of the array.The second line contains N space-separated integers.
Output Format
Print an integer the minimum number of moves to transform the given array into a zigzag array.
'''
n=int(input())
arr=list(map(int,input().split()))
result1=0
for i in range(0,n,2):
    start=arr[i]
    if i>0:
        if (arr[i-1]-1<start):
            start=arr[i-1]-1
    if i+1!=n:
       if arr[i+1]-1<start:
           start=arr[i+1]-1
    result1=result1+arr[i]-start
    print("result1=",result1)
result2=0
for i in range(1,n,2):
    start=arr[i]
    if i>0:
        if (arr[i-1]-1<start):
            start=arr[i-1]-1
    if i+1 != n:
        if arr[i+1]-1<start:
            start=arr[i+1]-1
    result2=result2+arr[i]-start
    print("result2=",result2)
if result1<result2:
    print(result1)
else:
    print(result2)