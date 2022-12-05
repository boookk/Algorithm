import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    answer = 1
    clothes = {}
    
    n = int(input())
    
    for _ in range(n):
        v, k = input().split()
        
        if not clothes.get(k):
            clothes[k] = set()
        clothes[k].add(v)
    
    for key in clothes.keys():
        answer *= len(clothes[key]) + 1
    
    print(answer - 1)
