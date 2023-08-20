'''Pairs
PrepBuddy has M pairs of integers, each integer is between 1 and N, inclusive. The pairs are (A1,B1),(A2,B2),…,(AM,BM).
PrepBuddy asks you to check if there exist two integers x and y (1≤x<y≤N) such that in each given pair at least one
integer is equal to x or y.
Input
The first line contains two space-separated integers N and M — the upper bound on the values of integers in the pairs,
and the number of given pairs.The next M lines contain two integers each, the ith of them contains two space-separated
integers Ai and Bi (1≤Ai,Bi≤N,Ai≠Bi) — the integers in the ith pair.
Output
Print YES if there exist two integers x and y (1≤x<y≤N) such that in each given pair at least one integer is equal to
x or y. Otherwise, print NO.'''
n,m=map(int,input().split())
arr_x=[]
arr_y=[]
flag=0
for i in range(m):
    x,y=map(int,input().split())
    arr_x.append(x)
    arr_y.append(y)
for i in range(m-1):
    if (arr_x[i]==arr_y[i+1] or arr_y[i]==arr_x[i+1]):
        flag=1
    elif (arr_x.index(arr_x[i],i,m)==arr_y.index(arr_y[i],i,m)):
        flag=1
    else:
        flag=0
if flag==1:
    print("YES")
else:
    print("NO")
# freq_x=[0]*(n+1)
# freq_y=[0]*(n+1)
# for i in range(m):
#     freq_x[arr_x[i]]+=1
#     freq_y[arr_y[i]]+=1
# for i in range(n+1):
#     print("X=",freq_x[i],end=" ")
#     print("Y=",freq_y[i],end=" ")
