#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):
    var1 = 0
    var2 = 0
    var1 = x1 + v1
    var2 = x2 + v2
    count = 1
    while (5000):
        if (var1 == var2):
            return "YES"
        elif (count == 5000):
            return "NO"
        else:
            var1 = var1 + v1
            var2 = var2 + v2
        count = count + 1


if __name__ == '__main__':

    x1V1X2V2 = input().split()

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])

    result = kangaroo(x1, v1, x2, v2)

    print(result)
