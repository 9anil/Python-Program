'''Find Even and Odd elements
Let's add more mathematics with arrays.You are given an array of size N, containing N integers.
Teacher is asking you to print all the even elements in the first line and all odd elements in the second line.
The array will contain at least one even and one odd element.
Input Format
First line contains integer N. Second line contains N space-separated integers.
Output Format
In the first line print space-separated Even elements.In the first line print space-separated Odd elements.'''
N=int(input())
arr=list(map(int,input().split()))
even=[]
odd=[]
for i in range(N):
    if arr[i]%2==0:
        even.append(arr[i])
    else:
        odd.append(arr[i])
for i in range(len(even)):
    print(even[i],end=" ")
print()
for i in range(len(odd)):
    print(odd[i],end=" ")
print()