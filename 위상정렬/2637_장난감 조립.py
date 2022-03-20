import sys
from collections import deque

input = sys.stdin.readline

n = int(input())    # 1부터 n - 1까지 기본 부품과 중간 부붐의 번호, n은 완제품의 번호
m = int(input())
graph = [[] for _ in range(n + 1)]
inDegree = [0] * (n + 1)
dp = [[0] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    x, y, k = map(int, input().split())         # x를 만드는 데에 y가 k개 필요하다.
    graph[y].append([x, k])
    inDegree[x] += 1

queue = deque()
for i in range(1, n + 1):
    if inDegree[i] == 0:
        queue.append(i)

while queue:
    now = queue.popleft()

    for next, k in graph[now]:
        inDegree[next] -= 1

        if sum(dp[now]) == 0:       # 기본 부품이면
            dp[next][now] += k
        else:
            for i in range(1, n + 1):
                dp[next][i] += dp[now][i] * k
        if inDegree[next] == 0:
            queue.append(next)

for i in range(1, n + 1):
    if dp[n][i]:
        print(i, dp[n][i])
