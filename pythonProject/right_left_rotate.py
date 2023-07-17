t=int(input())
while t>0:
    n,k=map(int,input().split())
    arr=list(map(int,input().split()))
    # Right Rotation Array...
    for i in range(k):
        temp=arr[n-1]
        for j in range(n-1,-1,-1):
            arr[j]=arr[j-1]
        arr[0]=temp
    print("*** Right rotation of array ***")
    for i in range(n):
        print(arr[i],end=" ")
#     # Left Rotation Array..
#     print("\n*** Left Rotation Array ***")
#     for i in range(k):
#         temp1=arr[0]
#         for j in range(0,n-1):
#             arr[j]=arr[j+1]
#         arr[n-1]=temp1
#     for i in range(n):
#         print(arr[i],end=" ")
    print()
    t=t-1
#def left_rotation(arr,n):
#     temp=arr[0]
#     for i in range(0,n-1):
#         arr[i]=arr[i+1]
#     arr[n-1]=temp
# def print_left_rotation(arr,n):
#     for i in range(n):
#         print(arr[i],end=" ")
#     print()
# def right_rotation(arr,n):
#     temp=arr[n-1]
#     for i in range(n-1,0,-1):
#         arr[i]=arr[i-1]
#     arr[0]=temp
# def print_right_rotation(arr,n):
#     for i in range(n):
#         print(arr[i],end=" ")
#     print()
# def main():
#     t=int(input())
#     while t>0:
#         n,k=map(int,input().split())
#         arr=list(map(int,input().split()))
#         for i in range(k):
#             # left_rotation(arr,n)
#             right_rotation(arr,n)
#         # print_left_rotation(arr,n)
#         print_right_rotation(arr,n)
#         t=t-1
# if __name__=='__main__':
#     main()
# Array rotation by reversal algorthim ---------------------------------------------------------------------->>>>>>>
# def reversalRightRotation_algo(arr,i,j):
#     while i<j:
#         temp=arr[i]
#         arr[i]=arr[j]
#         arr[j]=temp
#         i+=1
#         j-=1
# def print_reversalRightRotation(arr,n):
#     for i in range(0,n):
#         print(arr[i],end=" ")
#     print()
# def main():
#     t=int(input())
#     while t>0:
#         n,k=map(int,input().split())
#         arr=list(map(int,input().split()))
#         reversalRightRotation_algo(arr,n-k,n-1)
#         reversalRightRotation_algo(arr,0,n-k-1)
#         reversalRightRotation_algo(arr,0,n-1)
#         print_reversalRightRotation(arr,n)
#         t-=1
# if __name__=='__main__':
#     main()
# def reversalLeftRotation_algo(arr,i,j):
#     while i<j:
#         temp=arr[i]
#         arr[i]=arr[j]
#         arr[j]=temp
#         i+=1
#         j-=1
# def print_reversalLeftRotation(arr,n):
#     for i in range(n):
#         print(arr[i],end=" ")
#     print()
# def main():
#     t=int(input())
#     while t>0:
#         n,k=map(int,input().split())
#         arr=list(map(int,input().split()))
#         reversalLeftRotation_algo(arr,0,k-1)
#         reversalLeftRotation_algo(arr,k,n-1)
#         reversalLeftRotation_algo(arr,0,n-1)
#         print_reversalLeftRotation(arr,n)
#         t-=1
# if __name__=='__main__':
#     main()


