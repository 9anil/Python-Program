class x:
    pass
class y:
    pass
class z:
    pass
class p(x,y):
    pass
class q(y,z):
    pass
class r(p,q):
    pass
print(r.mro())
