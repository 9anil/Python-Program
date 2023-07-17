for i in range(1,6):
    for j in range(1,i+1):
        print(j,end="")
    print("")


# To print another pattern
space=8
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end="")
    for k in range(1,space+1):
        print(" ",end="")
    space=space-2
    for j in range(i,0,-1):
        print(j,end="")
    print("")
