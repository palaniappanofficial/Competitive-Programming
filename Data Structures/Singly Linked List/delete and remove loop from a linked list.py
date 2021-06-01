class Linklist:
    def __init__(self, data):
        self.data = data
        self.next = None
class Linkedlist:
    def __init__(self):
        self.head=None
    def addElement(self,data):
        node=Linklist(data)
        node.next=self.head
        self.head=node
    def printdata(self):
        temp=self.head
        while(temp is not None):
            print(temp.data)
            temp=temp.next
    def detectloop(self):
        slow=self.head
        fast=self.head
        while(slow and fast and fast.next):
            slow=slow.next
            fast=fast.next.next
            if(slow==fast):
                self.removeloop(slow)
                return 1
        return 0
    def removeloop(self,loop):
        ptr1=self.head
        while(1):
            ptr2 = loop
            while(ptr2.next!=loop and ptr2.next!=ptr1):
                ptr2=ptr2.next
            if(ptr2.next==ptr1):
                break
            ptr1=ptr1.next
        ptr2.next=None


obj=Linkedlist()
obj.addElement(50)
obj.addElement(40)
obj.addElement(30)
obj.addElement(20)
obj.addElement(10)
obj.head.next.next.next.next.next=obj.head.next.next
obj.detectloop()
obj.printdata()