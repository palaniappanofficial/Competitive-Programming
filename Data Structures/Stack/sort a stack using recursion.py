def createstack():
    stack=[]
    return stack
def pushelement(stack,item):
    stack.append(item)
def sortstack(stack,item):
    if len(stack)==0 or item>stack[-1]:
        stack.append(item)
    else:
        temp=stack.pop()
        sortstack(stack,item)
        stack.append(temp)
def stacktraverse(stack):
    if len(stack)!=0:
        temp=stack.pop()
        stacktraverse(stack)
        sortstack(stack,temp)


stack=createstack()
pushelement(stack,30)
pushelement(stack,50)
pushelement(stack,-15)
pushelement(stack,-2)
pushelement(stack,-26)
pushelement(stack,-8)
pushelement(stack,32)
pushelement(stack,97)
print(stack)
stacktraverse(stack)
print(stack)