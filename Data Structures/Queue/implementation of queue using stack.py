class Queue:
    def __init__(self):
        self.array=[]
        self.temparray=[]
    def enqueue(self,data):
        while len(self.array)!=0:
            self.temparray.append(self.array[-1])
            self.array.pop()
        self.array.append(data)
        while len(self.temparray)!=0:
            self.array.append(self.temparray[-1])
            self.temparray.pop()
    def dequeue(self):
        if len(self.array)==0:
            print("Queue is Empty")
            return
        element=self.array[-1]
        self.array.pop()
        return element
obj=Queue()
obj.enqueue(1)
obj.enqueue(2)
obj.enqueue(3)
obj.enqueue(4)
a=obj.dequeue()
print(a)