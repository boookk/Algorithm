"""
3차원 리스트라는 점이 헷갈렸다.
그래도 BFS 풀듯이 풀면 풀리는 문제!

처음에 제출했더니 시간 초과가 발생해서 PyPy3로 다시 제출했다.
그랬더니 Exit code가 0이 아니여서 오류가 발생하였다.
이것은 종료 함수의 코드를 -1로 설정하였기 때문이다.
세 번째 제출에서는 종료 함수의 코드를 0으로 설정하였는데, 틀렸다고 결과가 나왔다.
그래서 고민하다가 3차원 데이터를 입력받는 부분에서 sys.stdin.readline()으로 바꾸었더니 성공했다!

@@ 느낀 점 @@
1. 종료 함수를 사용할 때는 exit code는 0으로 설정한다.
2. 시간 초과가 아니라, 틀렸다고 결과가 나와도 sys.stdin.readline()을 사용하면 성공할 수 있다.
"""
import sys
from collections import deque


m, n, h = map(int, input().split())
queue = deque()
graph = []
for i in range(h):
    tmp = []
    for j in range(n):
        tmp.append(list(map(int, sys.stdin.readline().split())))
        for k in range(m):
            if tmp[j][k] == 1:
                queue.append((i, j, k))
    graph.append(tmp)

# 위, 아래, 왼쪽, 오른쪽, 앞, 뒤
dx = [-1, 0, 1, 0, 0, 0]
dy = [0, -1, 0, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

while queue:
    z, x, y = queue.popleft()

    for i in range(6):
        nx = x + dx[i]
        ny = y + dy[i]
        nz = z + dz[i]

        if -1 < nx < n and -1 < ny < m and -1 < nz < h and graph[nz][nx][ny] == 0:
            graph[nz][nx][ny] = graph[z][x][y] + 1
            queue.append((nz, nx, ny))

result = 0
for i in graph:
    for j in i:
        for k in j:
            if k == 0:
                print(-1)
                exit(0)
            result = max(result, k)

print(result - 1)
