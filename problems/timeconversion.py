#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    #
    # Write your code here.
    #
    a=[]
    new=[]
    fmt=""
    time=""
    last=""
    b=[]
    string=""
    s=str(s)
    a=s.split(":")
    fmt=a[len(a)-1]
    new[:]=fmt
    time=new[-2]
    if(time=="P"):
        if(int(a[0]!="12")):
            a[0]=str(int(a[0])+12)
    elif(time=="A"):
        if(int(a[0]=="12")):
            a[0]=str(int(a[0])-12)
            if(int(a[0])<10):
                a[0]=str(0)+a[0]
    last=a.pop()
    b[:]=last
    b=b[:-2]
    for i in b:
        string=string+i
    a.append(string)
    return (a[0]+":"+a[1]+":"+a[2])

if __name__ == '__main__':

    s = input()

    result = timeConversion(s)

    print(result)
