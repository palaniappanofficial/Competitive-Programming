tuples=[(1,9),(7,2),(4,),(28,29),(3,27),(2,),(87,)]
k=1
a=filter(lambda x:len(x)!=k,tuples)
for i in a:
    print(i)