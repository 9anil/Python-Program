class car:
    def __init__(self,gears,seats,speed):
        self.gears=gears
        self.seats=seats
        self.speed=speed
    def speedup(self):
        print("Speed increase")
    def apply_break(self):
        print("Speed Decreasing")
    def movement(self):
        print("Car is moving forword and backword")
class BMW(car):
    def __init__(self,miles,gears,seats,speed):
        self.miles=miles
        super(BMW, self).__init__(gears,seats,speed)
    def luxury(self):
        print("BMW is a luxurious care")
#    pass
s1=BMW("15 KM per Liter",5,4,240)
print(s1.gears,s1.seats,s1.speed)
print(s1.miles)
s1.speedup()
s1.apply_break()
s1.luxury()
class toyota(car):
    pass
class flying_car(car):
    def movement(self):#Method overriding
        print("Car is moving forword,backword,UP and down also")

f1=flying_car(5,6,400)
f1.movement()
t1=toyota(4,8,220)
print(t1.gears)
print(t1.seats)
print(t1.speed)
t1.speedup()
t1.apply_break()