import sys
sys.setrecursionlimit(10**4)
input = sys.stdin.readline


def dfs(day, history, yesterday):
    if day == n:
        print(*history, sep='\n')
        exit(0)

    for today in graph[day]:
        if yesterday != today and not visited[day][today - 1]:
            visited[day][today - 1] = True
            dfs(day + 1, history + [today], today)


n = int(input())
graph = [list(map(int, input().split()))[1:] for _ in range(n)]

visited = [[False] * 10 for _ in range(n + 1)]
dfs(0, [], 0)
print(-1)
