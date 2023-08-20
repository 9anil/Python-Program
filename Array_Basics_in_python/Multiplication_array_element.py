# s="a@b@c@d"
# a=list(s.partition("@"))
# print(a)
# b=list(s.split("@",4))
# print(b)

''' Multiplication of Array elements
Ravi is happy that you solved the previous questions, just to be sure that you are comfortable with operators and
arrays, he is giving you this problem.You are provided with the size of the array represented by N and N array elements.
You need to output the multiplication of all the elements. See sample test cases for better understanding.
Input Format
First line contains the value of test case variable T.Then follows T test cases.First line contains N representing the
size of the array.Second line contains N space-separated integers.
Output Format
For each test case T on a new line, print the multiplication.'''
T=int(input())
while T>0:
    N=int(input())
    arr=list(map(int,input().split()))
    multi=1
    for i in range(N):
        multi*=arr[i]
    print(multi)
    T-=0
