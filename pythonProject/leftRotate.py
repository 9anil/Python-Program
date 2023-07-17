# def leftRotate(arr,n):
#     temp=arr[0]
#     for i in range(0,n-1):
#         arr[i]=arr[i+1]
#     arr[n-1]=temp
# def printArr(arr,n):
#     for i in range(n):
#         print(arr[i],end=" ")
#     print()
# def main():
#     t=int(input())
#     while t>0:
#         n,k=map(int,input().split())
#         arr=list(map(int,input().split()))
#         for i in range(k):
#             leftRotate(arr,n)
#         printArr(arr,n)
#     t=t-1
# if __name__=='__main__':
#     main()
t=int(input())
while t>0:
    n,k=map(int,input().split())
    arr=list(map(int,input().split()))
    for i in range(k):
        temp=arr[n-1]
        for j in range(n-1,-1,-1):
            arr[j]=arr[j-1]
        arr[0]=temp
    # for i in range(k,n):
    #     temp=arr[n-1]
    #     for j in range(n-1,k-1,-1):
    #         arr[j]=arr[j-1]
    #     arr[k]=temp
    # for i in range(0,n):
    #     temp=arr[n-1]
    #     for j in range(n-1,0,-1):
    #         arr[j]=arr[j-1]
    #     arr[0]=temp
    for i in range(n):
        print(arr[i],end=" ")
    t=t-1