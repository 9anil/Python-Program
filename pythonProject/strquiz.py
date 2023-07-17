t=int(input())
while t>0:
  s=input()
  flag=0
  for i in range(len(s)-1):
    if(s[i]!='a' and s[i]!='e' and s[i]!='i' and s[i]!='o' and s[i]!='u' and s[i]!='n'):
      flag=0
    if(s[i+1]!='a' and s[i+1]!='e' and s[i+1]!='i' and s[i+1]!='o' and s[i+1]!='u' and s[i+1]!='n'):
      flag=0
    if (i==len(s)-1 and s[i]=='a' or s[i]=='e' or s[i]=='i' or s[i]=='o' or s[i]=='u' or s[i]=='n'):
      flag=1
  if flag==1:
    print("Yes")
  else:
    print("No")
  t=t-1

  t = int(input())
  while t > 0:
    s = input()
    freq = [0] * 26
    min = -1
    for i in range(len(s)):
      freq[ord(s[i]) - 97] += 1
    for i in range(26):
      print(chr(freq[i]+97), end=" ")
  t -= 1

  t = int(input())
  while t > 0:
    s = input()
    freq = [0] * 26
    for i in range(len(s)):
      freq[ord(s[i]) - 97] += 1
    for i in range(26):
      if (freq[i] > 1):
        print(chr(i + 97) + "=",freq[i], end=" ")
      else:
        print(-1)
    print()
    t = t - 1