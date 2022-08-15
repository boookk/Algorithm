import sys
from collections import deque
input = sys.stdin.readline


def bfs(v):
    visited[v] = True
    queue = deque([v])
    idx = 0

    while queue:
        for e in queue:
            teams[idx].append(e)

        for _ in range(len(queue)):
            x = queue.popleft()

            for v in hate[x]:
                if not visited[v]:
                    visited[v] = True
                    queue.append(v)
        idx ^= 1


n = int(input())
hate = [[]] + [list(map(int, input().split()))[1:] for _ in range(n)]

visited = [False] * (n + 1)
teams = [[], []]

for i in range(1, n + 1):
    if not visited[i]:
        bfs(i)

for i in range(2):
    print(len(teams[i]))
    print(*sorted(teams[i]))
