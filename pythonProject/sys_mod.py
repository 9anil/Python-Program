# import sys
# for i in sys.stdin:
#     if 'p'==i.rstrip():
#         break
#     print(f'Input:{i}')
# print("Exit")
# import sys
# t=int(input())
# while t>0:
#   ans=sys.maxsize
#   n=int(input())
#   arr=list(map(str,input().split()))[:n]
#   for i in range(n):
#     count=0
#     for j in range(n):
#       tmp=arr[j]+arr[j]
#       print(tmp)
#       index=tmp.find(arr[i])
#       print(index)
#       if (index==len(arr[i])):
#         print(-1)
#       count+=index
#     ans=min(count,ans)
#   print(ans)
#   t-=1
# import sys
# t=int(input())
# while t>0:
#   ans=sys.maxsize
#   print(ans)
#   n=int(input())
#   arr=list(map(str,input().split()))[:n]
#   for i in range(n):
#     count=0
#     for j in range(n):
#       tmp=arr[j]+arr[j]
#       print(tmp)
#       print(arr[i])
#       index=tmp.find(arr[i])
#       print(index,ans)
#       if (index==len(arr[i])):
#         print(-1)
#       count+=index
#       print(count,ans)
#     ans=min(count,ans)
#   print(ans)
# #   t-=1
# import sys
# t=int(input())
# while t>0:
#   n=int(input())
#   arr=[]
#   ans=sys.maxsize
#   #sum=0
#   for i in range(n):
#     arr.append(input())
#   for i in range(n):
#     count=0
#     for j in range(n):
#       tmp=arr[j]+arr[j]
#       index=tmp.find(arr[i])
#       print(index,ans)
#       if index==len(arr[i]):
#         print(-1)
#       count=count+index
#     ans=min(count,ans)
#   # sum+=ans
#     print(ans)
#   t-=1
# t=int(input())
# while t>0:
#   s=input()
#   mid=len(s)//2
#   flag=0
#   for i in range(len(s)):
#     if s[:mid]=='('*mid and s[mid:]==')'*mid:
#       flag=1
#     elif s[:mid]==')' and s[mid:]=='(' and len(s)==2:
#       flag=1
#     elif s[:mid]=='('*(mid-1)+')'and s[:mid]==')'*(mid-1)+'(':
#       flag=1
#     else:
#       flag=0
#   if flag==1:
#     print("Yes")
#   else:
#     print("No")
#   t-=1
# s='(())'
# mid=len(s)//2
# print(s[:mid]
t=int(input())
while t>0:
  n=[]
  flag=0
  for i in input().split():
    n.append(int(i))
  for ele in range(len(n)):
    print(n[ele])
  # for i in range(1,len(n)-1):
  #   if(n[i-1]+n[i]==n[i+1]):
  #     flag=1
  #   else:
  #     flag=0
  # if flag==1:
  #   print("yes")
  # else:
  #   print("no")
  t-=1