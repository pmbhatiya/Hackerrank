# Python Introduction to Sets HackerRank solution

def average(array):
    s=set(array)
    length=s.__len__()
    sum_set=sum(s,0)
    return float(sum_set/length)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)