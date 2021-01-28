class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def breadthfirstsearch(root):
    if root is None:
        return None
    queues = []
    array=[]
    queues.append(root)
    array.append(root.data)
    while (len(queues)>0):
        refer=queues.pop(0)
        if refer.left:
            queues.append(refer.left)
            array.append(refer.left.data)
        if refer.right:
            queues.append(refer.right)
            array.append(refer.right.data)
    return array
root=node(1)
root.left=node(2)
root.right=node(3)
root.left.left=node(4)
root.left.right=node(5)
b=breadthfirstsearch(root)
print(b)
