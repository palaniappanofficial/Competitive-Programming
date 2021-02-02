#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    plus=0
    minus=0
    zero=0
    floatplus=0
    floatminus=0
    floatzero=0
    for i in arr:
        if i<0:
            minus=minus+1
        elif i>0:
            plus=plus+1
        else:
            zero=zero+1
    print("{:.6f}".format(float(plus)/float(len(arr))))
    print("{:.6f}".format(float(minus)/float(len(arr))))
    print("{:.6f}".format(float(zero)/float(len(arr))))
if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
