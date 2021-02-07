def createstack():
    stack=[]
    return stack
def pushelement(stack,element):
    return stack.append(element)
def deleteelement(stack):
    if len(stack)==0:
        return ""
    else:
        return stack.pop()
def reverseelement():
    stack=createstack()
    string=""
    userInput=input("Enter a String:")
    for i in range(len(userInput)):
        pushelement(stack,userInput[i])
    for i in range(len(userInput)):
        string=string+deleteelement(stack)
    print(string)
reverseelement()


