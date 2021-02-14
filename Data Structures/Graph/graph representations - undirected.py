class vertex:
    def __init__(self,data):
        self.data=data
        self.next=None
class graph:
    def __init__(self,vertices):
        self.vertices=vertices
        self.totalvertex=[None]*self.vertices
    def appendnode(self,source,destination):
        node=vertex(destination)
        node.next=self.totalvertex[source]
        self.totalvertex[source]=node

        node=vertex(source)
        node.next=self.totalvertex[destination]
        self.totalvertex[destination]=node
    def printgraph(self):
        for i in range(self.vertices):
            print("Adjacent Vertices for",i)
            lastnode=self.totalvertex[i]
            print("head",end=" ")
            while lastnode:
                print("--->",lastnode.data,end=" ")
                lastnode=lastnode.next

            print("\n")
a=5
obj=graph(a)
obj.appendnode(0,1)
obj.appendnode(0,4)
obj.appendnode(1,2)
obj.appendnode(1,3)
obj.appendnode(1,4)
obj.appendnode(2,3)
obj.appendnode(3,4)
obj.printgraph()

