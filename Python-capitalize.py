#Python Capitalize HackerRank Solution 
#!/bin/python3

import math
import os
import random
import re
import sys

def solve(s):
    f_name = s.split(' ')
    return ' '.join((word.capitalize() for word in f_name))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()