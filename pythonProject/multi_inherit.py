class car:
    def __init__(self,gears,seats,speed):
        self.gears=gears
        self.seats=seats
        self.speed=speed
    def hundai(self):
        print("This is a hundai company car")
    def volvo(self):
        print("this is volvo company car")
    def movement(self):
        print("Hundai car are very good and high price car")
class maruti:
    def __init__(self,brand):
        self.brand=brand
class vancar(car):
    def __init__(self,milease,color,gears,seats,speed):
        self.milease=milease
        self.color=color
        super(vancar,self).__init__(gears,seats,speed)
class smallcar(car):
    def movement(self):
        print("Small car is a good car for lower class family!")
class compo_car(car,maruti):
    def __init__(self,gears,seats,speed,brand):
        car.__init__(self,gears,seats,speed)
        maruti.__init__(self,brand)
v1=vancar(15,"Red",5,8,"Max 180 KM/HOUR")
print(v1.milease,v1.color,v1.gears,v1.seats,v1.speed)
v1.hundai()
v1.volvo()
v1.movement()
s1=smallcar(4,4,"MAX 150 KM/HOUR")
print(s1.gears,s1.seats,s1.speed)
s1.volvo()
s1.movement()
print("-----------------------------------------------")
c1=compo_car(2,3,123,"Nano_car")
print(c1.brand)
