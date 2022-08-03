"""
플로이드 와샬 알고리즘
자신이 갈 수 있는 노드들은 자기보다 작은 사람들이며,
자신에게 오는 경로가 있는 노드들은 자기보다 큰 사람들이다.
이 둘의 합이 자신을 제외한 n-1인 경우 자신의 순서를 알 수 있는 것이다.
PyPy3 제출.
"""
import sys
input = sys.stdin.readline


n, m = map(int, input().split())
graph = [[0] * n for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a - 1][b - 1] = 1

for k in range(n):
    for i in range(n):
        for j in range(n):
            if graph[i][k] + graph[k][j] == 2:
                graph[i][j] = 1

ans = 0
for i in range(n):
    cnt = 0
    for j in range(n):
        cnt += graph[i][j] + graph[j][i]
    
    if cnt == n - 1:
        ans += 1

print(ans)
