# Python Set .discard(), .remove() & .pop() HackerRank solution

n = int(input())
s = set(map(int, input().split()))
length=int(input())
for i in range(length):
    operation=input().split()
    
    if operation[0]=='pop':
        getattr(s,operation[0])()
    else:
        getattr(s,operation[0])(int(operation[1]))
print(sum(s))