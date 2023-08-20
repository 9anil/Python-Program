# Brute force  approach
n=int(input())
age=list(map(int,input().split()))
count=0
for A in range(n):
    for B in range(n):
        if A != B:
            if ((age[B]<= (0.5*age[A]+7)) or (age[B]>100 and age[A]<100) or (age[B]>age[A])):
                continue
            else:
                count+=1
print(count)

#  Optimize approach
ans=0
freq=[0]*(max(age)+1)
for i in range(n):
    freq[age[i]]+=1
for A in range(len(freq)):
    for B in range(len(freq)):
        if ((B<=(0.5*A+7)) or (B>100 and A<100) or (B>A)):
            continue
        ans=ans+freq[A]*freq[B]
        if A==B:
            ans=ans-freq[A]
print("Optimize=",ans)