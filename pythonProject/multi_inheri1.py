class base1:
    def __init__(self,fname,lname,age):
        self.firstname=fname
        self.lastname=lname
        self.age=age
    def occupation(self):
        print("Hard working former")
    def liveing(self):
        print("Currently living in Nawab Gunj Village")
class base2:
    def __init__(self,name,age2):
        self.name=name
        self.age2=age2
        self.occuption="Studay"
class compo_base(base1,base2):#multi inheritance
    def __init__(self,fname,lname,age,name,age2):
        base1.__init__(self,fname,lname,age)
        base2.__init__(self,name,age2)
c1=compo_base("Ramesh","Singh",55,"Raju Sing",20)
print(c1.firstname,c1.lastname,c1.age)
print(c1.name,c1.age,c1.occuption)
c1.occupation()
print("-------------------------------------------------")
class b1(base1):
    def occupation(self):#method overriding
        print("Occupation is Gram Pradhan of My Village")
b=b1("Raghu","Rao",33)
print(b.firstname,b.lastname,b.age)
b.occupation()
class c(base2):
    pass
c=c("Amrita Ghose",35)
print(c.name,c.age2,c.occuption)
