def left_ArrayRotation(arr,N):
    temp=arr[0]
    for i in range(N-1):
        arr[i]=arr[i+1]
    arr[N-1]=temp
def PrintArray(arr,N):
    for i in range(N):
        print(arr[i],end=" ")
    print()
def main():
    T=int(input())
    while T>0:
        N,K=map(int,input().split())
        arr=list(map(int,input().split()))
        for i in range(K):
            left_ArrayRotation(arr,N)
        PrintArray(arr,N)
        T-=1
if __name__=='__main__':
    main()