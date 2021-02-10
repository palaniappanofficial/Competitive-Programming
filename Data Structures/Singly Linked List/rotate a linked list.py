class Linkedlist:
    def __init__(self,data):
        self.data=data
        self.next=None
class Linklist:
    def __init__(self):
        self.head=None
    def insertfirst(self,data):
        newlist=Linkedlist(data)
        newlist.next=self.head
        self.head=newlist
    def rotatelinkedlist(self,k):
        count=1
        current=self.head
        while(count<k and current is not None):
            current=current.next
            count=count+1
        knode=current
        while(current.next is not None):
            current=current.next
        current.next=self.head
        self.head=knode.next
        knode.next=None
    def printlinkedlist(self):
        temp=self.head
        while(temp):
            print(temp.data, "",end="")
            temp=temp.next
        print("\n")
obj=Linklist()
obj.insertfirst(1)
obj.insertfirst(2)
obj.insertfirst(3)
obj.insertfirst(4)
obj.insertfirst(5)
obj.printlinkedlist()
obj.rotatelinkedlist(3)
obj.printlinkedlist()