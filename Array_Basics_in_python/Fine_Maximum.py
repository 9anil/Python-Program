'''Find Maximum
Abishek always participates in competitive programming because he enjoys solving competitive programming questions.
PrepBuddy organizes a coding competition and announces a big price for the winner. He gave an array and asked to
find the maximum difference between indexes (j–i) such that arr[j]>arr[i] where j>i. Abhishek is not able to solve
this problem, but he wants to win this competitive programming. So he is asking for help.
Input Format
The first line contains an integer N size of the array.The second line contains N space-separated integers.
Output Format
Print the maximum difference, if the maximum difference is not present then print −1.'''

# n=int(input())
# arr=list(map(int,input().split()))
# maxdiff_index=0
# maxdiff_value=0
# flag=0
# for i in range(n):
#     for j in range(n-1,i,-1):
#       if i<j:
#         if ((arr[j]-arr[i])>maxdiff_value) and ((j-i)>maxdiff_index):
#           maxdiff_index=j-i
#           flag=1
# if flag==1:
#   print(maxdiff_index)
# else:
#   print(-1)

print("<------------------------------------Optimize approach--------------------------------->")
def maximum_diff(arr,i,j):
    maxdiff=0
    flag=0
    for i in range(0,j+1):
        if i!=j:
            if ((arr[j]-arr[i])>0 and (j-i)>maxdiff) :
                maxdiff=j-i
                flag=1
    j-=1
    for j in range(j,0,-1):
        i=0
        if i!=j:
            if ((arr[j] - arr[i]) > 0 and (j - i) > maxdiff):
                maxdiff = j - i
                flag = 1
        i+=1
    if flag==1:
        print(maxdiff)
    else:
        print(-1)
def main():
    n=int(input())
    arr=list(map(int,input().split()))
    maximum_diff(arr,0,n-1)
if __name__=='__main__':
    main()
