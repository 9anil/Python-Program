'''Arithmetic Progression
You are given an integer sequence a1,a2,...,an of length n. You have to analyze the sequence. The task is to find
all values of x, for which these two conditions hold.
1. x occurs in sequence a.
2. Consider all positions of numbers x in the sequence a (such i, that ai = x). These numbers, sorted in
the increasing order, must form an arithmetic progression. Find all x that meets the problem conditions.
Input format
The first line contains integer n.The next line contains integers  a1,a2, ..., an separated by space.
Output format
In the first line print integer M — the number of valid x. On each of the next M lines print two integers x and px,
where x is current suitable value, px is the common difference between numbers in the progression (if x occurs exactly
once in the sequence, px must equal 0). Print the pairs in the order of increasing x.'''

n=int(input())
arr=list(map(int,input().split()))
freq=[0]*(max(arr)+1)
for i in range(n):
    freq[arr[i]]+=1
for i in range(n):
