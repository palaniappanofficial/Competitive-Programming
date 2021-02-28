# Method 1
a=(10,4,6,9)
b=(5,2,3,3)

c=[element1^element2 for element1,element2 in zip(a,b)]
print(c)

# Method 2

from operator import xor
d=list(map(xor,a,b))
print(d)