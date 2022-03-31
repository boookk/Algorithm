from collections import deque


def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx <= -1 or nx >= n or ny <= -1 or ny >= m:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))


n, m = map(int, input().split())
graph = [list(map(int, list(input()))) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
bfs(0, 0)
print(graph[n-1][m-1])


"""
처음에 DFS로 풀다가 하나의 테스트 케이스를 해결하지 못해서 원인이 무엇인지 고민하였다.
DFS를 사용하는 경우 시작 지점부터 끝 지점까지 모든 노드를 방문하게 된다. 그래서 DFS를 최적의 해를 찾는 경우에 사용한다.
이 문제는 최단 경로를 찾아야 하기 때문에 BFS를 사용해야 한다.
"""
