from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph=defaultdict(list)
    def insertgraph(self,key,value):
        self.graph[key].append(value)
    def breadthfirst(self,key):
        queue=[]
        queue.append(key)
        visible=[False]*(max(self.graph)+1)
        visible[key] =True
        while queue:
            value=queue.pop(0)
            print(value,end=" ")
            for i in self.graph[value]:
                if visible[i]==False:
                    queue.append(i)
                    visible[i]=True

obj=Graph()
obj.insertgraph(0,1)
obj.insertgraph(0,2)
obj.insertgraph(1,2)
obj.insertgraph(2,0)
obj.insertgraph(2,3)
obj.insertgraph(3,3)
obj.breadthfirst(2)