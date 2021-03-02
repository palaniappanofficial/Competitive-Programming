#Packing and Unpacking For List

def addsum(*array):
    return sum(array)
array=[1,2,3,4]
a=addsum(*array)
print(a)
c=addsum(*[20,5,3,4,5,6,1])
print(c)

def calculate(a,b,c):
    return a+b+c
a=[1,2,3]
b=calculate(*a)
print(b)

def printlist(*string):
    list1=list(string)
    list1[0]="Hi"
    print(list1)
obj=printlist("Hello","Palaniappan","How are You")


#Packing and Unpacking For Dictionaries

def printdict(**dictionary):
    print(dictionary)

def printanotherdict(Name,Age,Profession):
    print(Name,Age,Profession)

dictionary={"Name":"Palaniappan","Age":"20","Profession":"Student"}

obj=printdict(**dictionary)
obj=printanotherdict(**dictionary)

