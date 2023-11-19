#!/bin/python3

import math
import os
import random
import re
import sys
import functools

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def printRatio(arr, total):
    print (len(arr) / len(total))

def plusMinus(arr):
    printRatio(list(filter(lambda a : (a > 0) , arr )), arr)
    printRatio(list(filter(lambda a : (a < 0) , arr )), arr)
    printRatio(list(filter(lambda a : (a == 0) , arr )), arr)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)