# t=int(input())
# while(t>0):
#     s1=input()
#     s2=[]
#     freq=[0]*26
#     flag=0
#     min=10001
#     for i in range(len(s1)):
#         freq[ord(s1[i].lower())-97]+=1
#     for i in range(26):
#         if freq[i]==1:
#             s2.append(chr(i+97))
#     for i in range(len(s1)):
#         for j in range(len(s2)):
#             if s1[i].lower()==s2[j]:
#                 flag=1
#                 if min>i:
#                     min=i
#     if flag==0:
#         print(-1)
#     else:
#         print(min)
#     t-=1
st="Prep Bytes"
print(st[0])
print(st[4])
print(st[9])
print(st[-1])
print(st[-9])
print(st[-10])
print(st[0:4])
print(st[3:])
print(st[4:9])
print(st[0:4]+st[4:])
print(st[5:]+st[:4])
print(st[-6:-1])
print(st[-6:-10])
print(st[::-1])
print(st[0::-1])
print(st[6:1:-1])
print(st[5:8:-1])
print(st[-7:-1:-1])
print(st[-7:-10:-1])
# String is immutable, need to any change first convert string into a list then modify it
st=list(st)
#st[4]="+"
print(st)
st1=""
st2="1"
print(st1.join(st))
print(st2.join(st))
st3="".join(map(str,st))
print(st3)
s1=['p','r','e','p',4,8.9,'b',77,'t']
s2="".join(map(str,s1))
print(s2)
s3=""
print(s3.join(s1)) # It can be give an error because it also integer contains to avoide this error use map function.
