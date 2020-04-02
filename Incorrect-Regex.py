# Python Incorrect Regex HackerRank solution

import re
n=int(input())

for i in range(n):
    try:
        re.compile(input())
        valid=True
    except re.error as e:
        valid=False
    print(valid) 