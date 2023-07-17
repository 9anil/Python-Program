t=int(input())
while t>0:
    s=input()
    #s1=list(s)
    freq=[0]*26
    #print(freq)
    flag=0
    for i in range(len(s)):
        freq[ord(s[i].lower())-97]+=1
    for i in range(26):
        if freq[i]>1:
            #print(chr(97+i),"=",freq[i],end=" ")
            print("{}:{}".format(chr(97+i),freq[i]),end=" ")
            flag=1
    if (flag==0):
        print(-1)
    else:
        print()
    t-=1

import re
t=int(input())
while t>0:
  s=input()
  count=0
  for i in range(len(s)):
    for j in range(len(s)):
      if i!=j:
        if (re.search(" *aman* ",s[i:j+1])):
          count+=1
  print(count)
  t=t-1

  t = int(input())
  while t > 0:
      tcard, tsuit = map(str, input().split())
      card, suit = list(map(str, input().split()))
      t -= 1