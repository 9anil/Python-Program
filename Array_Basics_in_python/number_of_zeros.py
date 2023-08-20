def zeros(n):
    count=0
    for i in range(1,n+1):
        j=i
        while j%5==0:
            count+=1
            j=j//5
    print(count)
def main():
    n=int(input())
    zeros(n)
if __name__=='__main__':
    main()