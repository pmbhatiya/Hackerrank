#Python Mutations HackerRank Solution 

def mutate_string(string, position, character):
    l=[]
    l=string;
    new=""
    for i in range(position):
        new+=l[i]
    new+=character
    for i in range(position+1,len(l)):
        new+=l[i]    
    return new

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)