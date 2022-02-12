from collections import deque


def bfs(x, y):
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx <= -1 or nx >= n or ny <= -1 or ny >= m:
                continue
            if not graph[nx][ny]:
                continue
            queue.append((nx, ny))
            graph[nx][ny] = 0


T = int(input())
result = []
# 테스트 케이스 개수 T만큼 반복
for _ in range(T):
    m, n, k = map(int, input().split())
    graph = [[0] * m for _ in range(n)]
    for _ in range(k):
        i, j = map(int, input().split())
        graph[j][i] = 1
    count = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j]:
                graph[i][j] = 0
                bfs(i, j)
                count += 1
    result.append(count)
print(*result, sep='\n')


"""
헷갈린 점.
배추지렁이가 현재 위치한 지점으로부터 상하좌우로만 움직일 수 있다고 생각했다.
그러나 다른 배추와 상하좌우로 인접해 있다면 인접한 지점으로부터 상하좌우로도 움직일 수 있다.
즉, 배추가 상하좌우로 인접한 하나의 구간에는 하나의 배추흰지렁이가 필요하다.
"""
