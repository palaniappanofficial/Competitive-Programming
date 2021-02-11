class Linkedlist:
    def __init__(self,data):
        self.data=data
        self.next=None
class Linklist:
    def __init__(self):
        self.head=None
    def addlast(self,data):
        newlist=Linkedlist(data)
        if self.head is None:
            self.head=newlist
            return
        temp = self.head
        while temp.next is not None:
            temp=temp.next
        temp.next=newlist
    def mergetwosortedlinkedlist(self,headA,headB):
        dummynode=Linkedlist(0)
        tail=dummynode
        while True:
            if headA is None:
                tail.next = headB
                break
            if headB is None:
                tail.next = headA
                break
            if headA.data<=headB.data:
                tail.next=headA
                headA=headA.next
            else:
                tail.next=headB
                headB=headB.next
            tail=tail.next
        return dummynode.next

    def printlinkedlist(self):
        temp=self.head
        while temp:
            print(temp.data,end=" ")
            temp=temp.next
        print("\n")

obj=Linklist()
obj.addlast(10)
obj.addlast(13)
obj.addlast(14)
obj.addlast(15)
obj.printlinkedlist()

obj2=Linklist()
obj2.addlast(1)
obj2.addlast(2)
obj2.addlast(3)
obj2.addlast(4)
obj2.addlast(5)
obj2.printlinkedlist()

obj.head=obj.mergetwosortedlinkedlist(obj.head,obj2.head)

obj.printlinkedlist()