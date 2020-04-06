# Python Collections.deque() HackerRank solution

from collections import deque

N=int(input())
D=deque()
for i in range(N):
    name=list(map(str,input().split()))
    
    if name[0]=='pop' or name[0]=='popleft' or name[0]=='popright':
        getattr(D,name[0])()
    else:
        getattr(D,name[0])(int(name[1]))

for i in range(len(D)):
    print(D[i],end=" ")