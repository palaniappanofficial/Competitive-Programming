class Solution:
    def solve(self, a, b):
        c=[]
        for i in a:
            c.append(i)
        for i in b:
            c.append(i)
        c.sort()
        return c
a=[8,5,9]
b=[6,7,2]
obj=Solution()
value=obj.solve(a,b)
print(value)
