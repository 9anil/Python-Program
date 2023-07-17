t=int(input())
while t>0:
    n,q=map(int,input().split())
    st=input()[:n]
    freq=[0]*26
    for i in range(len(st)):
        freq[ord(st[i].lower())-97]+=1
    for i in range(26):
        print(freq[i],end=" ")
    print()
    # for i in range(26):
    #     if (freq[i]==0):
    #         continue
    #     if (freq[i]<=sn):
    #         print(chr(i+97),"in Isolation center")
    #     if (freq[i]>sn):
    #         print(chr(97+i),"in pending quea")
    for i in range(q):
        m=int(input())
        count=0
        for j in range(26):
            if (freq[j]>m):
                count+=freq[j]-m
        print(count)
    t=t-1
