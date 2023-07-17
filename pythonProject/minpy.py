# t=int(input())
# while t>0:
#     arr=[]
#     min=10000000000
#     max=0
#     for element in input().split():
#         arr.append(int(element))
#     for i in arr:
#         print(i,end=" ")
#     print("")
#     for i in range(len(arr)):
#         if arr[i]<min:
#             min=arr[i]
#         if arr[i]>max:
#             max=arr[i]
#     print("Min=",min)
#     print("max=",max)
#     t=t-1
# s="a@b@C@d"
# a=list(s.partition("@"))
# print(a)
# b=list(s.split("@",6))
# print(b)
#Multiplication of array element
# t=int(input())
# while t>0:
#     n=int(input())
#     arr=list(map(int,input().split()))
#     M=1
#     for i in range(n):
#         M=M*arr[i]
#     # if 1<n<9:
#     #     A=[]
#     #     M=1
#     #     for i in input().split():
#     #        A.append(int(i))
#     #     for i in A:
#     #         M=M*i
#     print(M)
#     t=t-1

# Odd and Even number from array
# t=int(input())
# while t>0:
#     n=int(input())
#     arr=list(map(int,input().split()))
#     even=[]
#     odd=[]
#     for i in range(n):
#         if arr[i]%2==0:
#             even.append(arr[i])
#         else:
#             odd.append(arr[i])
#     for i in even:
#         print(i,end=' ')
#     print()
#     for i in odd:
#         print(i,end=" ")
#     t=t-1
# def test_case(arr, n, s):
#     for i in range(n-1, -1, -1):
#         s = s + arr[i]
#         if arr[i] == 1:
#             print(i)
#             break
#     if s == 0:
#         print(-1)
#
#
# def main():
#     t = int(input())
#     while t > 0:
#         n = int(input())
#         arr = list(map(int, input().split()))
#         s = 0
#         test_case(arr, n, s)
#         t = t - 1
#
#
# if __name__ == '__main__':
#     main()

t = int(input())
while t > 0:
    n = int(input())
    arr = list(map(int, input().split()))
    if 2 <= n <= 100:
        if arr[0] > arr[1]:
            print(0, end=" ")
        for i in range(1, n - 1):
            if arr[i] > arr[i + 1] and arr[i] > arr[i - 1]:
                print(i, end=" ")
        if arr[n - 1] > arr[n - 2]:
            print(n - 1, end=" ")
        for i in range(n-1):
            if arr[i] == arr[i + 1]:
                print(-1)
        print()
    else:
        print("Enter correct values")
    t = t - 1
