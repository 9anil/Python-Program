'''Maximum Difference
You are given an array A consisting of N integers, you have to find the maximum value of the following expression:
|Ai−Aj| + |i−j| where, 0<=i,j<N and Ai,Aj are the Array elements.
Input Format
The first line of input contains an integer T denoting the number of test cases.Each test case contains two lines,
the first line contains integer N where N is the number of elements in the array.Second line contains N space separated
integers Ai.
Output Format
Print the maximum value of the above given expression, for each test case separated by a new line.
Constraints
1≤T≤100
1≤N≤10^5
0≤Ai≤10^5
Note: Use Fast I/O (scanf/printf or any other ways) to handle large test files.'''
# t=int(input())
# while t>0:
#     n=int(input())
#     result=0
#     arr=list(map(int,input().split()))
#     for i in range(n):
#         for j in range(n):
#             if result<(abs(arr[i]-arr[j])+abs(i-j)):
#                 result=abs(arr[i]-arr[j])+abs(i-j)
#     print(result)
#     t-=1
def main():
    t=int(input())
    while t>0:
        n=int(input())
        arr=list(map(int,input().split()))
        arr1=[]
        arr2=[]
        for i in range(n):
            arr1.append(arr[i]+i)
            arr2.append(arr[i]-i)
        max1=arr1[0]
        min1=arr1[0]
        for i in range(n):
            if max1<arr1[i]:
                max1=arr1[i]
            if min1>arr1[i]:
                min1=arr1[i]
        result1=max1-min1
        max2=arr2[0]
        min2=arr2[0]
        for i in range(n):
            if max2<arr2[i]:
                max2=arr2[i]
            if min2>arr2[i]:
                min2=arr2[i]
        result2=max2-min2
        if result1>result2:
            print(result1)
        else:
            print(result2)
        t-=1
if __name__=='__main__':
    main()