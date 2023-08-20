'''Quality Factor
Rahul and PrepBuddy have a collection of two types of stones-Red and Black. Red stone has quality factor=1 and Black
stone has quality factor=-1.PrepBuddy has a normal container containing N bags and each bag contains a mixture of Red
and Black stones. The overall quality factor of the bag is calculated by the summation of the quality factor of Red
and Black stones.
For example, if a bag contains 5 Red stones and 3 Black stones than the quality factor of bag=5(1)+(3(−1))=5−3=2.
Let's denote the quality factor of each bag by b1,b2,b3,b4....bn.
Rahul has a magical container that contains N empty bags(quality factor =0 for each bag). The magic of the container is,
if a Red stone is added to the ith bag then quality factor of each bag from (i to N) in the container increases by 1
and if a Black stone is added to the ith bag then quality factor of each bag from (i to N) in the container decreases by
1.Let's denote quality factor of each bag owned by Rahul as r1,r2,r3,r4...rn.
Rahul's task is to make r1=b1,r2=b2,r3=b3,...rn=bn. To achieve this he can only perform one operation i.e he can either
add a Red stone or he can add a Black stone into any ith bag. He can perform this operation any number of times.
Help Rahul to determine the minimum number of times this operation needs to be performed to complete his task.
Note - Consider you have an unlimited supply of stones.
Input format
First line contains N representing the number of bags.Second line contains N space-separated integers representing
the quality factor of each bag owned by PrepBuddy.
Output format
For each test case, print the minimum number of moves required to complete Rahuls's task.
(output should be printed on a new line for each test case).'''
n=int(input())
prepb_qf=list(map(int,input().split()))
rahul_qf=[0]*n
count=0
current=0
for i in range(n):
    count=count+abs(prepb_qf[i]-current)
    current=prepb_qf[i]
print(count)

