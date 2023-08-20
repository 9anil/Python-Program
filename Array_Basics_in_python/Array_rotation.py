# Array Rotation.
'''Array Rotation
Ravi has recently heard about something called Array Rotation and wants you to write a code for rotating an array.
So what happens in array rotation is, you are given an integer array A of size N and an integer K, you have to
rotate the array in the right direction by K steps(See test cases for better understanding). The task is to print
the rotated array.
Input Format
The first line contains an integer T denoting the number of test cases.Each test case consists of two lines.
The first line contains N, number of elements in the array and K number of steps.The Second line contains N
space-separated integers.
Output Format
For each test case on a new line, print the rotated array.'''
# def right_rotation(arr,N,K):
#     for r in range(K):
#         temp=arr[N-1]
#         for i in range(N-1,0,-1):
#             arr[i]=arr[i-1]
#         arr[0]=temp
#     for i in range(N):
#         print(arr[i],end=" ")
#     print()
# def main():
#     T=int(input())
#     while T>0:
#         N,K=map(int,input().split())
#         arr=list(map(int,input().split()))
#         right_rotation(arr,N,K)
#         T-=T
# if __name__=='__main__':
#     main()
print("<-----------------------------------*****------------------------------------------------->")
def right_ArrayRotation(arr,N):
    temp=arr[N-1]
    for i in range(N-1,0,-1):
        arr[i]=arr[i-1]
    arr[0]=temp
def PrintArr(arr,N):
    for i in range(N):
        print(arr[i],end=" ")
    print()
def main():
    T=int(input())
    while T>0:
        N,K=map(int,input().split())
        arr=list(map(int,input().split()))
        for i in range(K):
            right_ArrayRotation(arr,N)
        PrintArr(arr,N)
        T-=1
if __name__=='__main__':
    main()