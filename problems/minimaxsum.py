#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    sum = 0
    mini = 0
    maxi = 0
    array1 = []
    for i in range(len(arr)):
        for j in range(len(arr)):
            if (i == j):
                sum = sum
            else:
                sum = sum + arr[j]
        array1.append(sum)
        sum = 0
    mini = min(array1)
    maxi = max(array1)
    print(mini, maxi)


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
