# Python itertools.combinations_with_replacement() HackerRank solution

from itertools import combinations_with_replacement

string,length=input().split()
for i in combinations_with_replacement(sorted(string),int(length)):
    print(''.join(i))