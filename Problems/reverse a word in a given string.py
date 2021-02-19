def splitword(stringword):
    a=[]
    b=""
    a=stringword.split('.')
    i=len(a)-1
    while(i>=0):
        b=b+a[i]
        b=b+"."
        i=i-1
    print(b)
s="hi.palani.appan.how.are.you"
splitword(s)