# def example(b):
#     b = b + '4'
#     b = b*4
#     return b
# example("hello")
# def say(message, times = 1):
#     print(message * times)
# say('Prep')
# say('Bytes', 5)
# x = "abcdef"
# i="g"
# while i in x:
#     print(i, end=" ")
# True = False
# while True:
#     print(True)
#     break
# T=int(input())
# while T>0:
#   N=int(input())
# A=list(map(int,input().split()))
# print(A[::-1])
# t = int(input())
# while t > 0:
#     n = int(input())
#     arr = list(map(int, input().split()))
#     ans = 0
#     temp = [0] * n
#     for i in range(len(arr)):
#         temp[arr[i] - 1] = 1
#     for i in range(n):
#         if temp[i] == 0:
#             ans = i + 1
#     print(ans)
#     t = t - 1
# def missing_num(arr , n):
#     temp=[0]*n
#     for i in range(len(arr)):
#         temp[arr[i]-1] = 1
#     for i in range(n):
#         if temp[i] == 0:
#             print(i+1)
# def main():
#   t=int(input())
#   while t>0:
#     n=int(input())
#     arr=list(map(int,input().split()))
#     missing_num(arr,n)
# if __name__=='__main__':
#   main()
# n=int(input())
# arr=list(map(int,input().split()))
# n1=0
# n2=0
# for i in range(1,n-1,2):
#   if(arr[i]>arr[i-1] and arr[i]<=arr[i+1]):
#     arr[i+1]-=1
#     n1+=1
#   if (arr[i]<=arr[i-1] and arr[i]>arr[i+1]):
#     arr[i]-=1
#     n1+=1
#   if(arr[i]<=arr[i-1] and arr[i]<=arr[i+1]):
#     arr[i-1]-=1
#     arr[i+1]-=1
#     n1+=1
# for j in range(0,n-2,2):
#   if(arr[j]>arr[j+1] and arr[j+2]<=arr[j+1]):
#     arr[j+1]-=1
#     n2+=1
#   if (arr[j]<=arr[j+1] and arr[j+2]>arr[j+1]):
#     arr[j+1]-=1
#     n2+=1
#   if(arr[j]<=arr[j+1] and arr[j+2]<=arr[j+1]):
#     arr[j+1]-=1
#     n2+=1
# print(n1,n2)
# t=int(input())
# while t>0:
#   tcard=input()
#   hcard=list(map(str,input().split()))
#   flag=0
#   if (tcard[0]==hcard[0][0] or tcard[0]==hcard[1][0] or tcard[0]==hcard[2][0] or tcard[0]==hcard[3][0] or tcard[0]==hcard[4][0]):
#     flag=1
#   elif (tcard[1]==hcard[0][1] or tcard[1]==hcard[1][1] or tcard[1]==hcard[2][1] or tcard[1]==hcard[3][1] or tcard[1]==hcard[4][1]):
#     flag=1
#   else:
#     flag=0
#   if flag==0:
#     print("No")
#   else:
#     print("Yes")
#   t=t-1

# t=int(input())
# while t>0:
#   orign=input()
#   feak=input()
#   lpass=feak[0:2]
#   rpass=feak[2:len(feak)]
#   npass=rpass+lpass
#   lpass1=feak[0:len(feak)-2]
#   rpass1=feak[len(feak)-2:]
#   npass1=rpass1+lpass1
#   if (npass==orign):
#     print("Yes")
#   elif (npass1==orign):
#     print("Yes")
#   else:
#     print("No")
#   t-=1
t=int(input())
while t>0:
  n=int(input())
  for i in range(n):
    s=input()
  t-=1