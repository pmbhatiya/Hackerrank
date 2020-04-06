# Python Set Mutations HackerRank solution

N=int(input())
A=set(map(int,input().split()))
operation_size=int(input())
for i in range(operation_size):
    name,size=input().split()
    size=int(size)
    A1=set(map(int,input().split()))
    getattr(A,name)(A1)
    

print(sum(A))