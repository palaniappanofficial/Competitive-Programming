class Linkedlist:
    def __init__(self,data):
        self.data=data
        self.next=None
class Linklist:
    def __init__(self):
        self.head=None
    def insertlast(self,data):
        if self.head==None:
            newnode=Linkedlist(data)
            self.head=newnode
        else:
            temp=self.head
            newnode=Linkedlist(data)
            while(temp.next is not None):
                temp=temp.next
            temp.next=newnode
    def printlist(self):
        temp=self.head
        while(temp is not None):
            print(temp.data)
            temp=temp.next
def newnode(data):
    node=Linkedlist(data)
    return node
def printlist(linkedlist):
    temp=linkedlist
    while(temp is not None):
        print(temp.data)
        temp=temp.next
def finalnodeconnection(obj1):
    slow=obj1
    fast=obj1
    slow=slow.next
    fast=fast.next.next
    while(fast and fast.next is not None):
        if(slow==fast):
            break
        slow=slow.next
        fast=fast.next.next
    if(slow!=fast):
        return None
    slow=obj1
    while(slow!=fast):
        slow=slow.next
        fast=fast.next
    return slow


obj1=newnode(1)
obj1.next=newnode(2)
obj1.next.next=newnode(3)
obj1.next.next.next=newnode(4)
obj1.next.next.next.next=obj1.next
a=finalnodeconnection(obj1)
print("Final Node Connected to the Node",a.data)


