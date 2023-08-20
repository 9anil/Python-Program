'''Greater than neighbor
Rahul lives in a colony, where N houses are built in a single row numbered from 0 to N−1. The first house has the house
number 0, the second house has house number 1 and so on. Rahul wants to know the house number of the houses that are
paying more rent than both the neighbors in the row where Rahul lives.First and the last house will have only one neighbor.
Input format
First line contains test case T.T test cases follow,First line contains N representing the number of houses.
Second line contains the rent of the N houses.
Output format
For each test case, print house numbers(0-based indexing) that satisfy the above-mentioned condition.If no house
satisfies the criterion print −1.'''
T=int(input())
while T>0:
    N=int(input())
    rent=list(map(int,input().split()))
    max_neighbour=[]
    flag=0
    if rent[0]>rent[1]:
        max_neighbour.append(0)
        flag=1
    for  i in range(1,N-1):
        if rent[i-1]<rent[i]>rent[i+1]:
            max_neighbour.append(i)
            flag=1
    if rent[N-1]>rent[N-2]:
        max_neighbour.append(N-1)
        flag=1
    if flag==1:
        for index in max_neighbour:
            print(index,end=" ")
        print()
    else:
        print(-1)
    T-=1
