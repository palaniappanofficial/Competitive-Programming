def countoccurences(array):
    a=set(array)
    b=[]
    count=0
    dict={}
    for i in a:
        dict[i]="0"
    for i in array:
        dict[i]=int(dict[i])+1
    print(dict)
    for j in dict.values():
        b.append(j)
        if j>1:
            count=count+1
    print(count)
countoccurences([1,1,2,3,4,5,5,5,5,7,7,7,9,9])