
def oddnumbers(n,value,arr):
    if value>n:
        print(arr)
        return
    if value%2==1:
        arr.append(value)
    value=value+1
    oddnumbers(n,value,arr)



value=0
arr=[]
oddnumbers(100,value,arr)