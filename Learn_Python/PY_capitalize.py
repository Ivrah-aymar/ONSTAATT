#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    lis=s.split(" ")
    #print(lis)
    for x in range(len(lis)):
        lis[x]=lis[x].capitalize()
    s1=" ".join(lis)   
    #s1=" ".join(lis)
    return s1 
    #print(lis[x].capitalise() for x in range(len(lis)))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
