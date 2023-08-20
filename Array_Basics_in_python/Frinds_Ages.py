'''Friends Ages
Some students who took admission in college will send friend requests to other students. The list of their ages is
given and ages[i] is the age of the ith student.
Student A will not send a friend request to student B (A!=B) if any of the following conditions are true:
1. age [B]<=0.5*age[A]+7
2. age[B]>100 && age[A]<100
3.age[B]>age[A] Otherwise,A will send a friend request to B.Note that if A requests B, B does not necessarily request A.
Also, the student will not friend request themselves.
Find how many total friend requests are made?
Input Format
First-line contains an integer N size of the array.The second line contains N space-separated integers.
Output Format
Print the number of total requests made.'''
print("<------------------------------By Brute Force Approach-------------------------->")
n=int(input())
age=list(map(int,input().split()))
count=0
for A in range(n):
    for B in range(n):
        if A!=B:
            if (age[B]<=(0.5*age[A]+7) or (age[B]>100 and age[A]<100) or (age[B]>age[A])):
                continue
            else:
                count+=1
print(count)
print("<----------------------------------------- Optimize Approach--------------------------------->")
def main():
    n=int(input())
    age=list(map(int,input().split()))
    freq=[0]*(max(age)+1)
    request=0
    for i in range(n):
        freq[age[i]]+=1
    for A in range(len(freq)):
        for B in range(len(freq)):
            if (B<=(0.5*A+7) or (B>100 and A<100) or (B>A)):
                continue
            request+=freq[A]*freq[B]
            if A==B:
                request=request-freq[A]
    print(request)
if __name__=='__main__':
    main()