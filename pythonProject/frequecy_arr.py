t=int(input())
while t>0:
    n=int(input())
    arr=list(map(int,input().split()))
    freq=[0]*40
    count=0
    for i in range(n):
        freq[arr[i]]=freq[arr[i]]+1
    # for i in range(40):
    #     if(freq[i]>0):
    #         print(i,freq[i])
    flag=0
    for i in range(40):
        if (freq[i]>1):
            flag=1
            break
    if(flag==1):
        print("Element area not unique")
    else:
        print("Element are unique.")
    t=t-1
