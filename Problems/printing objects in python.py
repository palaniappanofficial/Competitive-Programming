class Main:
    def __init__(self,aval,bval):
        self.aval=aval
        self.bval=bval
    def __repr__(self):
        return "A Value : %s B Value : %s" %(self.aval,self.bval)
    def __str__(self):
        return "A : %s B : %s" %(self.aval,self.bval)


obj=Main(25,50)
print(obj) #Calls __str__ method
print([obj]) #Calls __repr__method