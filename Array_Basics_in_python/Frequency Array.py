# n=int(input())
# arr=list(map(int,input().split()))
# freq=[]
# for i in range(n):
#     count=1
#     for j in range(n):
#         if (i != j):
#             if arr[i]==arr[j]:
#                 count+=1
#     print(count)
T=int(input())
while T>0:
    n=int(input())
    arr=list(map(int,input().split()))[0:n]
    freq=[0]*(max(arr)+1)
    for i in range(n):
        freq[arr[i]]+=1
    for i in range(len(freq)):
        if freq[i]>0:
            print("{}={}".format(i,freq[i]),end=" ")
    print()
    T-=1
print("<--------------------------- Frequency by dictionary-------------------->")
ele_arr=[int(ele) for ele in input().split()]
ele_dict={}
for ele in ele_arr:
    if ele in ele_dict:
        ele_dict[ele]+=1
    else:
        ele_dict[ele]=1
for ele in ele_dict.items():
    print(ele,end=" ")
print()
for ele in ele_dict.values():
    print(ele,end=" ")
print([ele for ele in ele_dict.values() if ele>1])