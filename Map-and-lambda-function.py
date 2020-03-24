# Map and Lambda function in python Hackerrank solution

cube = lambda x: x**3
# complete the lambda function 

def fibonacci(n):
    # return a list of fibonacci numbers
    fibo=[0,1]
    for i in range(2, n):
        fibo.append(fibo[i-1] + fibo[i-2])
    
    return(fibo[0:n])    



if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))