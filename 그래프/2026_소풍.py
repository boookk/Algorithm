import sys
input = sys.stdin.readline


def dfs(student, friends):
    if len(friends) == k:
        print(*sorted(friends), sep='\n')
        exit(0)
    
    for i in range(student + 1, n + 1):
        if not visited[i]:
            for friend in friends:
                if friend not in graph[i]:
                    break
            else:
                visited[i] = True
                dfs(i, friends + [i])

    
    


k, n, f = map(int, input().split())

graph = [[] for _ in range(n + 1)]


for _ in range(f):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, n + 1):
    visited = [False] * (n + 1)
    visited[i] = True
    dfs(i, [i])

print(-1)
