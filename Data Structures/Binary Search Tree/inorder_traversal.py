class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
ary=[]
def inorder(root):
    if root.left:
        inorder(root.left)
    ary.append(root.data)
    if root.right:
        inorder(root.right)
    return ary
root=node(9)
root.left=node(7)
root.right=node(15)
root.left.left=node(5)
root.left.right=node(8)
b=inorder(root)
print(b)