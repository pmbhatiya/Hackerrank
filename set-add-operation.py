# Python set add() operation HackerRank solution

n=int(input())
s=set()
for i in range(n):
    s.add(input())
print(s.__len__())