T=int(input())
while T>0:
    n=int(input())
    arr=list(map(int,input().split()))
    min=100000001
    max=-1
    for i in range(n):
        if arr[i]<min:
            min=arr[i]
        if arr[i]>max:
            max=arr[i]
    print("Minimum value is {}".format(min))
    print("Maximum value is {}".format(max))
    T-=1