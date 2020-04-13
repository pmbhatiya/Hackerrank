# Python Min and Max HackerRank solution

import numpy as np

N,M=map(int,input().split())
array=np.array([input().split() for _ in range(N)],int)
print(np.max(np.min(array,axis=1)))