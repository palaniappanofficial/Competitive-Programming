from itertools import chain
a=[(1,2),(5,8),(9,7),(16,25),(27,22)]
print(a)
values=map(lambda b:b,chain.from_iterable(a))
sets=set()
print(values)
for i in values:
    for j in str(i):
        print(i,end=" ")
        sets.add(j)
print("\n")
print(sets)
