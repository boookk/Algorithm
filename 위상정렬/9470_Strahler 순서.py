import sys
from collections import deque

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    k, m, p = map(int, input().split())

    graph = [[] for _ in range(m + 1)]
    inDegree = [0] * (m + 1)
    dp = [[0] * (m + 1) for _ in range(m + 1)]
    end = 0

    for _ in range(p):
        a, b = map(int, input().split())
        graph[a].append(b)
        inDegree[b] += 1

    queue = deque()
    for i in range(1, m + 1):
        if inDegree[i] == 0:
            queue.append(i)
            dp[i][i] = 1

    while queue:
        x = queue.popleft()
        end = x

        for i in graph[x]:
            inDegree[i] -= 1

            dp[x][i] = dp[x][x]

            if inDegree[i] == 0:
                queue.append(i)
                max_ = 0
                count = 0
                for row in range(1, m + 1):
                    if max_ != 0 and dp[row][i] == max_:
                        count += 1
                    elif dp[row][i] > max_:
                        max_ = dp[row][i]
                        count = 1

                dp[i][i] = max_ if count == 1 else max_ + 1

    print(k, dp[end][end])
