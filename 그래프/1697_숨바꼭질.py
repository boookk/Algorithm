"""
다른 문제와 달리 입력이 배열 형태로 주어지지 않았기 때문에 직접 리스트를 선언하여 방문하였는지 확인하며 최단 시간을 구했다.
"""


from collections import deque


n, k = map(int, input().split())
MAX = 100000
visited = [0] * (MAX + 1)


def bfs():
    queue = deque()
    queue.append(n)

    while queue:
        x = queue.popleft()

        if x == k:
            print(visited[x])
            exit(0)

        for nx in (x - 1, x + 1, 2 * x):
            if 0 <= nx <= MAX and visited[nx] == 0:
                visited[nx] = visited[x] + 1
                queue.append(nx)


bfs()
