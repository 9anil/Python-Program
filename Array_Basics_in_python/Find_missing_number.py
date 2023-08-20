'''Find the Missing
Now, we are going to solve a very famous problem, most commonly known as find missing number problem.
What happens in this is, you are given an array A with N−1 elements having values from 1 to N with one element missing.
Your task is to find out the missing number.
Note - Do not use sorting or any in-built function to solve the question.
Input format
The first line contains an integer T, denoting the number of test cases.Then follows T test cases, and each test case
consists of two lines.The first line contains N.Second-line contains N−1 space-separated integers.
Output format
For each test case on a new line, print the missing number.'''
# T=int(input())
# while T>0:
#     N=int(input())
#     arr=list(map(int,input().split()))
#     temp=[0]*N
#     for i in range(len(arr)):
#         temp[arr[i]-1]=1
#     for i in range(N):
#         if temp[i]==0:
#             print(i+1)
#     T-=1
def find_missing_num(arr,N):
    temp=[0]*N
    for i in range(len(arr)):
        temp[arr[i]-1]=1
    for i in range(N):
        if temp[i]==0:
            print(i+1)
            #return i+1
def  main():
    T=int(input())
    while T>0:
        N=int(input())
        arr=list(map(int,input().split()))
        find_missing_num(arr,N)
        T-=1
if __name__=='__main__':
    main()