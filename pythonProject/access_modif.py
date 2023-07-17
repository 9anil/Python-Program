# access modifier (__) is used for private and (_) use for protected
class bank_account:
    __amount=1000#private access modifier can accessed only it self class
    _intrest=100#protected modifier it accessible by sub class
    def deposit(self,add,ins):
        self.__amount+=add
        self._intrest+=ins
    def debit(self,sub,sin):
        self.__amount-=sub
        self._intrest-=sin
    def printamount(self):
        print(self.__amount)
class user(bank_account):
    def tax(self):
        tx=self._intrest*0.5
        #tx1=self.__amount*0.2
        print(tx)
b=bank_account()
b.deposit(500,50)
#print(b.__amount)
b.printamount()
print(b._intrest)
b.debit(700,51)
print(b._intrest)
#print(b.__amount)
b.printamount()
u1=user()
u1.tax()