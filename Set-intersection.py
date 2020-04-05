# Python Set intersection() Operation HackerRank solution

N=int(input())
set_eng=set(map(int,input().split()))
M=int(input())
set_french=set(map(int,input().split()))
new_set=set_eng.intersection(set_french)
print(new_set.__len__())