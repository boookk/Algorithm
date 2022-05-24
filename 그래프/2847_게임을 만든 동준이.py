import sys


def dfs(i):
    global answer 
    
    if i < 0:
        return
    
    if level[i] >= level[i + 1]:
        tmp = level[i]
        level[i] = level[i + 1] - 1
        answer += tmp - level[i]
    
    dfs(i - 1)


input = sys.stdin.readline

n = int(input())
level = [int(input()) for _ in range(n)]

answer = 0
dfs(n - 2)
print(answer)
