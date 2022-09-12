import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline



def dfs(student):
    global ans
    visited[student] = True
    teams.append(student)
    idx = preference[student]
    
    if visited[idx]:
        if idx in teams:
            ans += len(teams[teams.index(idx):])
        return
    else:
        dfs(idx)


T = int(input())
for _ in range(T):
    n = int(input())
    preference = [0] + list(map(int, input().split()))
    visited = [False] * (n + 1)
    
    ans = 0
    for i in range(1, n + 1):
        if not visited[i]:
            teams = list()
            dfs(i)
    print(n - ans)
