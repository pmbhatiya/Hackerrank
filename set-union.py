# Python set Union Operation HackerRank solution

n=int(input())
eng=set(map(int,input().split()))
m=int(input())
french=set(map(int,input().split()))
merge=eng.union(french)
print(len(merge)) 