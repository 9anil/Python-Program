class trucaller:
    def call(self):
        print("Ringing for call")
class jiocaller:
    def call(self):
        print("Jiocaller app use for calling")
class phone:
    def callfunc(self,phoneApp):
        phoneApp.call()

phoneApp=trucaller()
#phoneApp=jiocaller()
p1=phone()
p1.callfunc(phoneApp)