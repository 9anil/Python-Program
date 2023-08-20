'''Find the Leader
A simple problem statement with no stories: Given an array of positive integer, find out all the elements that
are greater than or equal to all the elements to it's right side.
Input format
The first line contains an integer T, denoting the number of test cases.Then follows T test cases,and each test
case consists of two lines.The first line contains N.Second-line contains N space-separated integers.
Output format
For each test case on a new line, print the list of positive integers satisfying the above given condition.
Print from end element to start element.'''
def find_leader(arr,N):
    leader=[]
    leader.append(arr[N-1])
    last_num=arr[N-1]
    for i in range(N-2,-1,-1):
        if arr[i]>=arr[i+1] and arr[i]>=last_num:
            last_num=arr[i]
            leader.append(arr[i])
    for i in range(len(leader)):
        print(leader[i],end=" ")
    print()
def main():
    T=int(input())
    while T>0:
        N=int(input())
        arr=list(map(int,input().split()))
        find_leader(arr,N)
        T-=1
if __name__=='__main__':
    main()