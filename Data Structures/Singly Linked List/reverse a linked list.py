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
    def reverselinkedlist(self):
        prev=None
        current=self.head
        while(current is not None):
            next=current.next
            current.next=prev
            prev=current
            current=next
        self.head=prev
    def printlinkedlist(self):
        temp=self.head
        while(temp is not None):
            print(temp.data," ",end="")
            temp=temp.next
        print("\n")
obj=Linklist()
obj.insertfirst(3)
obj.insertfirst(2)
obj.insertfirst(1)
obj.insertfirst(4)
obj.insertfirst(5)
obj.insertfirst(6)
obj.printlinkedlist()
obj.reverselinkedlist()
obj.printlinkedlist()