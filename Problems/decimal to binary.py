#Using Built In Function
a=12
print(bin(a).replace("0b",""))

#Withou Using Built In Function
def dectobin(value):
    if value>=1:
        dectobin(value//2)
    print(value%2,end="")
dectobin(12)