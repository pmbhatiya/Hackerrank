# Python Exceptions HackerRank solution

N=int(input())
for i in range(N):
    try:
        a,b=map(int,input().split())
        try:
            print(int(a//b))
        except ZeroDivisionError as e1:
            print("Error Code:",e1)      
    except ValueError as e:
        print("Error Code:",e)  
    