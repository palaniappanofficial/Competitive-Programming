class Linkedlist:
    def __init__(self,data):
        self.data=data
        self.next=None
class Linklist:
    def __init__(self):
        self.head=None
    def insertfirst(self,data):
        newnode=Linkedlist(data)
        newnode.next=self.head
        self.head=newnode
    def countlinkedlist(self,temp):
        if(not temp):
            return 0
        return 1+self.countlinkedlist(temp.next)
    def count(self):
        temp = self.head
        return self.countlinkedlist(temp)

obj=Linklist()
obj.insertfirst(2)
obj.insertfirst(4)
obj.insertfirst(6)
obj.insertfirst(8)
obj.insertfirst(12)
a=obj.count()
print(a)