def balancingparanthesis(expr):
    stack=[]
    for each in expr:
        if each in ["(","{","["]:
            stack.append(each)
        else:
            lastcharacter=stack[len(stack)-1]
            if lastcharacter=="(":
                if each==")":
                    stack.pop()
            elif lastcharacter=="{":
                if each=="}":
                    stack.pop()
            elif lastcharacter=="[":
                if each=="]":
                    stack.pop()
    if stack:
        return False
    return True

expr="[{(([[]]))}]"
a=balancingparanthesis(expr)
print(a)