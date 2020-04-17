# Python Mean, Var, and Std HackerRank solution

import numpy as np

np.set_printoptions(legacy='1.13')
N,M=map(int,input().split())
array=np.array([list(map(int,input().split())) for _ in range(N)])

print(np.mean(array,axis=1))
print(np.var(array,axis=0))
print(np.std(array))
