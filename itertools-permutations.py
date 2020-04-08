# Python itertools.permutations() HackerRank solution

from itertools import permutations

string,length=input().split()
string=list(string)
string.sort()
length=int(length)
str_permutation=list(permutations(string,length))
for i in range(len(str_permutation)):
    char=''.join(tuple(str_permutation[i]))
    print(char)