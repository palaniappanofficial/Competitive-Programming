class Linkedlist:
    def __init__(self,data):
        self.data=data
        self.next=None
class Queue:
    def __init__(self):
        self.rear=None
        self.front=None
    def enqueue(self,data):
        newlist=Linkedlist(data)
        if self.rear is None:
            self.rear=newlist
            self.front=newlist
            return
        self.rear.next=newlist
        self.rear=newlist
    def dequeue(self):
        if self.front==None:
            return
        temp=self.front
        self.front=temp.next
        if self.front==None:
            self.rear=None

obj=Queue()
obj.enqueue(10)
obj.enqueue(20)
obj.enqueue(30)
obj.enqueue(40)
obj.dequeue()
print(obj.front.data)
print(obj.rear.data)