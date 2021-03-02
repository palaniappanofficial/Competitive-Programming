class A:
    def __init__(self):
        self.__hiddenvariable=0
    def addition(self,addvalue):
        self.__hiddenvariable=self.__hiddenvariable+addvalue
        print(addvalue)
obj=A()
obj.addition(20)
obj.addition(5)
#This line causes Error
# print(obj.__hiddenvariable)
print(obj._A__hiddenvariable)