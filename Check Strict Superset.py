# Python Check Strict Superset HackerRank solution

set_my=set(map(int,input().split()))
N=int(input())

flag=0
for i in range(N):
    set_check=set(map(int,input().split()))
    if set_my.issuperset(set_check)==False:
        print("False")
        flag=1
        break
if flag==0:
    print("True")
