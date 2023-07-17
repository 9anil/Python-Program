class student:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __add__(self,other):
        ans1=self.x + other.x
        ans2=self.y + other.y
        return "{} {}".format(ans1,ans2)
        #return ans1,ans2
    def __lt__(self, other):
        ans1=self.x+other.y
        ans2=self.y+other.x
        if(ans1<ans2):
            return True
        else:
            return False

s1=student(10,20)
s2=student(17,50)
s3=s1 + s2
#s3=student.__add__(s1,s2)
print(s3)
if s1<s2:
    print("s1 is smaller then s2")
else:
    print("s1 i larger then s2")