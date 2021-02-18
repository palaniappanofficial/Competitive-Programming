
def oddnumbers(n,value,arr):
    if value>n:
        return arr
    if value%2==1:
        arr.append(value)
    value=value+1
    a=oddnumbers(n,value,arr)
    return a



value=0
arr=[]
array=oddnumbers(100,value,arr)
print(array)