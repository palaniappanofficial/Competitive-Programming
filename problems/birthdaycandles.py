#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles):
    # Write your code here
    maxi=0
    count=0
    maxi=max(candles)
    for i in candles:
        if(maxi==i):
            count=count+1
    return count

candles=[5,2,6,6,8,9,1,9,9]
a=birthdayCakeCandles(candles)
print(a)