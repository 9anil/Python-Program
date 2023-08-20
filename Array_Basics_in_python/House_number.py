'''Minimum house number
Ravi lives in a colony, where N houses are built in a single row numbered from 0 to N−1. The first house has a
house number 0, the second house has a house number 1 and so on, every house pays some rent at the end of the month.
Help Ravi in finding out the house number of the house paying the minimum rent.
Note: All house rents are unique.
Input format
First line contains test case T.T test cases follow,First line contains N representing the number of houses.
Second line contains the rent of the N houses.
Output format
For each test case on a new line, print house numbers(0- based indexing) that satisfy the above-mentioned condition.
'''
T=int(input())
while T>0:
    N=int(input())
    rent=list(map(int,input().split()))
    min_rent=1001
    for i in range(N):
        if rent[i]<min_rent:
            min_rent=rent[i]
    for i in range(N):
        if min_rent==rent[i]:
            print(i)
    T-=1


