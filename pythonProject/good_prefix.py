t=int(input())
while t>0:
    st=input()
    k, x = map(int, input().split())
    count=0
    freq=[0]*26
    for ele in st:
        var=ord(ele)-97
        freq[var]+=1
        if (freq[var]>x):
            if k>0:
                freq[var]-=1
                k-=1
            else:
                break
        else:
            count+=1
    print(count)
    # for i in range(26):
    #     print(freq[i],end=" ")
    # count=0
    # for i in range(26):
    #     if freq[i]>1:
    #         count+=1
    # print(count)
    t=t-1