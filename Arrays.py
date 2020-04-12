# Python Arrays HackerRank solution

import numpy

def arrays(arr):
    result=numpy.array(arr[::-1],float)
    return result

arr = input().strip().split(' ')
result = arrays(arr)
print(result)