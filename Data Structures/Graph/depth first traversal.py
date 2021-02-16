# Python3 program to print DFS traversal
# from a given given graph
from collections import defaultdict


class Graph:

	def __init__(self):
		self.graph = defaultdict(list)

	def addEdge(self, u, v):
		self.graph[u].append(v)

	def DFSUtil(self, a, visited):

		visited.add(a)
		print(a, end=' ')

		for neighbour in self.graph[a]:
			if neighbour not in visited:
				self.DFSUtil(neighbour, visited)
	def DFS(self, v):

		visited = set()
		self.DFSUtil(v, visited)

obj = Graph()
obj.addEdge(0, 1)
obj.addEdge(0, 2)
obj.addEdge(1, 2)
obj.addEdge(2, 0)
obj.addEdge(2, 3)
obj.addEdge(3, 3)

obj.DFS(2)
