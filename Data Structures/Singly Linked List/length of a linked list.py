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
    def count(self):
        temp=self.head
        count=0
        while(temp):
            count=count+1
            temp=temp.next
        return count
obj=Linklist()
obj.insertfirst(10)
obj.insertfirst('a')
obj.insertfirst('b')
obj.insertfirst(20)
obj.insertfirst(30)
obj.insertfirst(40)
obj.insertfirst(50)
a=obj.count()
print(a)
