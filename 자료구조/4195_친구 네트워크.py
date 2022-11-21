import sys
input = sys.stdin.readline


def find(x):
    if friends[x] != x:
        friends[x] = find(friends[x])
    return friends[x]


def union(a, b):
    a = find(a)
    b = find(b)
    
    if a != b:
        friends[b] = a
        count[a] += count[b]


T = int(input())
for _ in range(T):
    n = int(input())
    
    friends = dict()
    count = dict()
    
    for _ in range(n):
        a, b = input().rstrip().split()
        
        if not friends.get(a):
            friends[a] = a
            count[a] = 1
        if not friends.get(b):
            friends[b] = b
            count[b] = 1
        
        union(a, b)
        print(count[find(a)])
