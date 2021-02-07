class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def inorder(root,arr):
    if root is None:
        return None
    if root.left:
        inorder(root.left,arr)
    arr.append(root.data)
    if root.right:
        inorder(root.right,arr)
    return arr

def nodescount(root):
    if root is None:
        return 0
    return nodescount(root.left)+nodescount(root.right)+1
def binaytreetobst(root,new):
    if root is None:
        return None
    binaytreetobst(root.left,new)
    root.data=new[0]
    new.pop(0)
    binaytreetobst(root.right,new)
    return root

def printbst(bst):
    if bst.left:
        printbst(bst.left)
    print(bst.data)
    if bst.right:
        printbst(bst.right)

def inordersort(root):
    new=[]
    arr=[]
    nodes=0
    nodes=nodescount(root)
    new=inorder(root,arr)
    new.sort()
    print(new)
    print(nodes)
    bst=binaytreetobst(root,new)
    printbst(bst)


root=node(10)
root.left=node(21)
root.right=node(32)
root.left.left=node(52)
root.left.right=node(12)
root.right.left=node(15)
root.right.right=node(9)
inordersort(root)