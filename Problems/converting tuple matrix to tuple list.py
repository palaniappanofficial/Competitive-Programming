#Method 1
test_list = [[(4, 5), (7, 8)],
             [(10, 13), (18, 17)],
             [(0, 4), (10, 1)]]
test=[element for i in test_list for element in i]
print(tuple(zip(*test)))

#Method 2
from itertools import chain
a=chain.from_iterable(test_list)
print(tuple(zip(*a)))
