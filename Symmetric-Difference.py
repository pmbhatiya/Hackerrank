# Python Symmetric Difference HackerRank solution

N=int(input())
set_list1=set(map(int,input().split()))
M=int(input())
set_list2=set(map(int,input().split()))
l=set_list2.difference(set_list1)
l1=set_list1.difference(set_list2)
l=l.union(l1)
l=list(l)
l.sort(reverse=False)
for i in range(len(l)):
    print(l[i],end="\n")