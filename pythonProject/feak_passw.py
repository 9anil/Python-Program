t=int(input())
while(t>0):
    orignal_pass=input()
    feak_pass=input()
    # Left rotation for 2-place
    lf1=feak_pass[0:2]
    rf1=feak_pass[2:]
    left=rf1+lf1
    # Right rotation for 2 place
    rf2=feak_pass[len(feak_pass)-2:]
    lf2=feak_pass[0:len(feak_pass)-2]
    right=rf2+lf2
    if(left==orignal_pass or right==orignal_pass):
        print("Yes")
    else:
        print("No")
    t=t-1
