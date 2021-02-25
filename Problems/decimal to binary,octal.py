#Using Built In Function
a=12
print(bin(a).replace("0b",""))
print(oct(a))

#Without Using Built In Function
def dectobin(value):
    if value>=1:
        dectobin(value//2)
    print(value%2,end="")
dectobin(12)


def dectooct(value):
    print("\n")
    digitval=1
    countval=0
    while(value!=0):
        remainder=value%8
        countval=countval+remainder*digitval
        digitval=digitval*10
        value=value//8
    print(countval)
dectooct(33)
