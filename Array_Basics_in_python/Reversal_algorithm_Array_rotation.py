# Reversal Algorithm
print("<--------------------Right Rotation by Reversal Algorithm -------------------------->")
def reversal_rightRotation(arr,i,j):
    while i<j:
        temp=arr[i]
        arr[i]=arr[j]
        arr[j]=temp
        i+=1
        j-=1
def printArr(arr,N):
    for i in range(N):
        print(arr[i],end=" ")
    print()
def main():
    T=int(input())
    while T>0:
        N,K=map(int,input().split())
        arr=list(map(int,input().split()))
        if K>N:
            K=K%N
        reversal_rightRotation(arr,N-K,N-1)
        reversal_rightRotation(arr,0,N-K-1)
        reversal_rightRotation(arr, 0, N-1)
        printArr(arr, N)
        T-=1
if __name__=='__main__':
    main()
print("<---------------------------------Left Rotation by reversal algorithm--------------------------->")
def reversal_leftRotation(arr,i,j):
    while i<j:
        temp=arr[i]
        arr[i]=arr[j]
        arr[j]=temp
        i+=1
        j-=1
def PrintArr(arr,n):
    for i in range(n):
        print(arr[i],end=" ")
    print()
def main():
    t=int(input())
    n,k=map(int,input().split())
    arr = list(map(int, input().split()))
    if k>n:
        k=k%n
    reversal_leftRotation(arr,0,k-1)
    reversal_leftRotation(arr,n-k-1,n-1)
    reversal_leftRotation(arr,0,n-1)
    PrintArr(arr,n)
    t-=1
if __name__=='__main__':
    main()