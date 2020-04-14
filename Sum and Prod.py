# Python Sum and Prod HackerRank solution

import numpy as np

N,M=map(int,input().split())
array=np.array([input().split() for _ in range(N)],int)
print(np.prod(np.sum(array,axis=0)))