n=int(input())
arr=list(map(int,input().split()))
uni=[0]*n
count=0
for i in range(n):
    uni[arr[i]]+=1
for i in range(n):
    if uni[i]==1:
        count+=1
print(count)
