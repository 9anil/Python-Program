def getunique_color(freq,i,j):
    count=0
    while i<j:
        if freq[i]==1:
            count+=1
        i+=1
    print(count)
def main():
    n=int(input())
    color=list(map(int,input().split()))
    freq=[0]*(max(color)+1)
    for i in range(n):
        freq[color[i]]+=1
    getunique_color(freq,0,len(freq))
if __name__=='__main__':
    main()
print("<------------------------- Other way in short code for unique color shirt-------------------->")
def getunique(arr):
    color_dic={}
    for i in arr:
        if i in color_dic:
            color_dic[i]+=1
        else:
            color_dic[i]=1
    print(len([ele for ele in color_dic if color_dic[ele]==1]))
n=int(input())
arr=[int(ele) for ele in input().split()]
getunique(arr)