#Python Nested-List HackerRank Solution 

if __name__ == '__main__':
    stu_list = list()
    n=int(input())
    for i in range(n):
        stu_list.append([input(), float(input())])

    scores = set([stu_list[x][1] for x in range(n)])
    scores = list(scores)
    scores.sort()

    stu_list = [x[0] for x in stu_list if x[1] == scores[1]]
    stu_list.sort()

    for my in stu_list:
        print (my)
