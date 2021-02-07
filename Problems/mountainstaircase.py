n=int(input())
for i in range(1,n+1):
    print(" "*(n-i),end="")
    if(i==1):
        print("*"*i,end="")
    else:
        print("*"*(i+(i-1)),end="")
    print(" "*(n-i))