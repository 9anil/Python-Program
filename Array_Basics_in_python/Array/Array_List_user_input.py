# Array/List user input: How to take list as input and create array
print("<------------------------------***----------------------------->")
arr=[]
for ele in input().split():
    arr.append(ele)
for i in range(len(arr)):
    print(arr[i],end=" ")
print(type(arr))
print("<-----------------------------***------------------------------->")
arr1=list(map(int,input().split()))
for i in range(len(arr1)):
    print(arr1[i],end=" ")