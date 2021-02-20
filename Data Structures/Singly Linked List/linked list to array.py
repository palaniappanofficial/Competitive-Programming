class Linkedlist:
    def __init__(self,data):
        self.data=data
        self.next=None
class Linklist:
    def __init__(self):
        self.head=None
    def insertlast(self,data):
        linklist=Linkedlist(data)
        if self.head==None:
            self.head=linklist
        else:
            temp=self.head
            while(temp.next is not None):
                temp=temp.next
            temp.next=linklist
    def printlist(self):
        temp=self.head
        while(temp is not None):
            print(temp.data,end=" ")
            temp=temp.next
        print("\n")
    def linkedlisttoarray(self):
        arr=[]
        temp=self.head
        while(temp is not None):
            arr.append(temp.data)
            temp=temp.next
        print(arr)

obj=Linklist()
obj.insertlast(1)
obj.insertlast(2)
obj.insertlast(8)
obj.insertlast(4)
obj.insertlast(5)
obj.printlist()
obj.linkedlisttoarray()



