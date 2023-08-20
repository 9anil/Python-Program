# Consecutive element sum..
# By normal/Brute force approach
n,k=map(int,input().split())
arr=list(map(int,input().split()))
#max_sum=[]
max=-1
for i in range(n):
    sum=0
    for j in range(i,k+i):
        if k+i<=n:
            sum=sum+arr[j]
    if sum>max:
        max=sum
#     max_sum.append(sum)
# for i in range(len(max_sum)):
#     if max_sum[i]>max:
#         max=max_sum[i]
print(max)
print("<-----------------------------------***---------------------------------------------->")
def getMaxSum(arr,n,k):
    max=-1
    for i in range(n-k+1):
        sum=0
        for j in range(i,k+i):
            sum+=arr[j]
        if sum>max:
            max=sum
    print(max)
def main():
    t=int(input())
    while t>0:
        n,k=map(int,input().split())
        arr=list(map(int,input().split()))
        getMaxSum(arr,n,k)
        t-=1
if __name__=='__main__':
    main()

print("<----------------------------------By Optimize approach ---------------------------------->")

n,k=map(int,input().split())
arr=list(map(int,input().split()))
sum=0
for i in range(k):
    sum+=arr[i]
max=sum
for i in range(k,n):
    sum=sum-arr[i-k]+arr[i]
    if sum>max:
        max=sum
print(max)