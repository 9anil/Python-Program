# class student:
#     def __init__(self):
#         self.sname="Amit Kumar"
#         self.age=19
#         self.standers=12
# # s1=student()
# # print(s1.sname,s1.age,s1.standers)
# def main():
#     s1=student()
#     print(s1.sname)
#     print(s1.age)
#     print(s1.standers)
# if __name__=='__main__':
#     main()

class mobile:
    wireless="Yes wireless service available"
    year="2011~2021"
    def __init__(self,bn,cl,pr):
        self.brandname=bn
        self.color=cl
        self.price=pr
    def calling(self):
        print("Use for calling purpose")
    def message(self):
        print("use for messaging to others")
def main():
    m1=mobile("Apple_iphone","Black",50000)
    m2=mobile("Nokia","Red_Blue",20000)
    print(m1.brandname,m1.color,m1.price)
    print(m2.brandname,m2.color,m2.price)
    m1.screen="LED_screen" #This is local for m1 only not accesssed by m2
    print(m1.screen)
    m2.calling()
    m2.message()
    print(m1.wireless,m1.year)
    print(m2.year,m2.wireless)
if __name__=='__main__':
    main()
