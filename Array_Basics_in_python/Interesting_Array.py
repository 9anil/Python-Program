print("<---------------------------------------Bruit Force approach-------------------------->")
# t=int(input())
# while t>0:
#     n=int(input())
#     arr=list(map(int,input().split()))
#     k=int(input())
#     min_i=n
#     max_j=-1
#     flag=0
#     for i in range(n):
#         for j in range(n):
#             if i != j and (k==arr[i]+arr[j]):
#                 flag=1
#                 if i<min_i:
#                     min_i=i
#                 if max_j<j:
#                     max_j=j
#     if flag==1:
#         print(min_i,max_j)
#     else:
#         print("No answer")
#     t-=1
print("<-------------------------------Optimize approach--------------------------------->")
T=int(input())
while T>0:
    N=int(input())
    arr=list(map(int,input().split()))
    K=int(input())
    flag=0
    i=0
    j=N-1
    while i<j:
        if ((arr[i]+arr[j])==K):
            flag=1
            print(i,j)
            break
        elif ((arr[i]+arr[j])>K):
            j-=1
        else:
            i+=1
    if flag==0:
        print("No answer")
    T-=1