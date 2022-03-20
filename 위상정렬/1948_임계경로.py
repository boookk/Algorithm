"""
위상정렬 출발지점에서 도착지점까지의 최장 경로를 구하고
역방향으로 된 그래프와 BFS 이용하여 각 지점까지의 최장 경로를 사용된 간선을 탐색한다.
"""
import sys
from collections import deque

input = sys.stdin.readline

n = int(input())    # 도시의 개수
m = int(input())    # 도로의 개수
inDegree = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]
rev_graph = [[] for _ in range(n + 1)]
dp = [0] * (n + 1)
for _ in range(m):
    start, end, time = map(int, input().split())
    graph[start].append([end, time])
    rev_graph[end].append([start, time])
    inDegree[end] += 1

start, end = map(int, input().split())
queue = deque([(start, 0)])

while queue:
    x, time = queue.popleft()

    for i, t in graph[x]:
        inDegree[i] -= 1
        dp[i] = max(dp[i], dp[x] + t)
        if inDegree[i] == 0:
            queue.append((i, dp[i]))

queue = deque([end])
count = 0
visited = [False] * (n + 1)
while queue:
    x = queue.popleft()

    for i, t in rev_graph[x]:
        if dp[i] + t == dp[x]:
            count += 1
            if not visited[i]:
                queue.append(i)
                visited[i] = True

print(dp[end])
print(count)
