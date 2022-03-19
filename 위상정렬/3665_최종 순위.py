import sys
from collections import deque

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    inDegree = [0] * (n + 1)
    queue = deque()
    graph = [[] for _ in range(n + 1)]
    result = []

    tmp = list(map(int, input().split()))  # 작년 순위
    for i in range(n):
        for j in range(i + 1, n):
            v, u = tmp[i], tmp[j]
            graph[v].append(u)
            inDegree[u] += 1
    
    m = int(input())        # 등수가 바뀐 쌍의 수
    for _ in range(m):
        i, j = map(int, input().split())
        if j in graph[i]:
            graph[j].append(i)
            graph[i].remove(j)
            inDegree[i] += 1
            inDegree[j] -= 1
        else:
            graph[i].append(j)
            graph[j].remove(i)
            inDegree[i] -= 1
            inDegree[j] += 1

    for i in range(1, n + 1):
        if inDegree[i] == 0:
            queue.append(i)

    while queue:
        x = queue.popleft()
        result.append(x)

        for i in graph[x]:
            inDegree[i] -= 1

            if inDegree[i] == 0:
                queue.append(i)

    if len(result) == n:
        print(*result)
    else:
        print('IMPOSSIBLE')
