# n,k=map(int,input().split())
# arr=list(map(int,input().split()))
# max=0
# for i in range(0,n-k+1):
#     sum=0
#     for j in range(i,i+k):
#         sum+=arr[j]
#     if sum>max:
#         max=sum
# print(max)
# def main():
#     t=int(input())
#     while t>0:
#         n,k=map(int,input().split())
#         arr=list(map(int,input().split()))
#         max=-1
#         for i in range(n-k+1):
#             sum=0
#             for j in range(i,i+k):
#                 sum+=arr[j]
#             if sum>max:
#                 max=sum
#         print(max)
#         t-=1
# if __name__=='__main__':
#     main()

# def main():
#     t=int(input())
#     while t>0:
#         n,k=map(int,input().split())
#         arr=list(map(int,input().split()))
#         max=0
#         sum=0
#         for i in range(0,k):
#             sum+=arr[i]
#         max=sum
#         for i in range(k,n):
#             sum=sum-arr[i-k]+arr[i]
#         if max<sum:
#             max=sum
#         print(max)
#     t-=1
# if __name__=='__main__':
#     main()

# t=int(input())
# while t>0:
#     n=int(input())
#     arr=list(map(int,input().split()))
#     num=int(input())
#     max=-1
#     min=-1
#     flag=0
#     for i in range(n-1):
#         for j in range(i+1,n):
#             if(arr[i]+arr[j]==num):
#                 flag=1
#                 if (j > max):
#                     max=j
#                     min=i
#                 elif (j==max and i<min):
#                     min=i
#                     max=j
#     if flag==0:
#         print(-1)
#     else:
#          print(min,max)
#     t=t-1

# n=int(input())
# arr=list(map(int,input().split()))
# k=int(input())
# i=0
# j=n-1
# flag=0
# while i<j:
#     sum=arr[i]+arr[j]
#     if sum==k:
#         flag=1
#         print(i,j)
#         break
#     elif sum>k:
#         j=j-1
#     else:
#         i=i+1
# if flag==0:
#     print(-1)

t = int(input())
while t > 0:
    n = int(input())
    arr = list(map(int, input().split()))
    k=int(input())
    mini = -1
    maxj = -1
    flag = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            if (arr[i] + arr[j] == k):
                flag = 1
                if j > maxj:
                    maxj = j
                if j == maxj and i > mini:
                    mini = i
        if flag == 0:
            print("No answere")
        else:
            print(mini, maxj)
    t = t - 1


