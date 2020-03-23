#python find second maximum HackerRank Solution

if __name__ == '__main__':
    n = int(input())
    arr =list(map(int, input().split(" "))) 
    maxa = max(arr)
    for i in range(0,n):
        if max(arr) == maxa:   
            arr.remove(max(arr))
    arr.sort(reverse=True)
    print(arr[0])    