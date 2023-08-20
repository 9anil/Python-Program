'''Last One
We all know computer understands only 0 and 1. Let's say you are given one such array A consisting only 0's and 1's.
Your task is to print the last index of the 1 present in the array.
Input Format
The first line contains an integer T denoting the number of test cases.Each test case consists of two lines.
The first line contains N, number of elements in the array.The second line contains N space-separated values either 0 or 1.
Output Format
For each test case on a new line, print index of the last 1 present in the array(0-based indexing).
If no one is present in the array print −1.
'''
T=int(input())
while T>0:
    N=int(input())
    binary_num=list(map(int,input().split()))
    index=0
    for i in range(N-1,-1,-1):
        if binary_num[i]==1:
            index=i
        else:
            index=-1
    print(index)
    T-=1
