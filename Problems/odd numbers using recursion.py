arr=[]
value=0
def oddnumbers(n):
    global value
    global arr
    if value>n:
        return arr
    if value%2==1:
        arr.append(value)
    value=value+1
    a=oddnumbers(n)
    return a



array=oddnumbers(100)
print(array)