"""
PyPy3 제출.
시간 제한 때문에 어려웠다.
통과할 수 있었던 결정적인 것은 거리를 구할 때 도시의 좌표를 직접 접근하기 보다, 변수에 할당하여 사용한 것이라고 생각한다.
"""
import sys
input = sys.stdin.readline


def get_dist(a, b):
    r1, c1 = cities[a]
    r2, c2 = cities[b]
    dist = abs(r1 - r2) + abs(c1 - c2)
    if teleport[a] == teleport[b] == 1 and t < dist:
        return t
    return dist


n, t = map(int, input().split())

INF = 2001
grid = [[INF] * n for _ in range(n)]
cities = list()
teleport = list()

for i in range(n):
    s, x, y = map(int, input().split())
    cities.append([x, y])
    teleport.append(s)

for i in range(n):
    for j in range(n):
        if i == j:
            continue
        grid[i][j] = get_dist(i, j)

for k in range(n):
    for i in range(n):
        for j in range(n):
            if grid[i][j] > grid[i][k] + grid[k][j]:
                grid[i][j] = grid[i][k] + grid[k][j]

m = int(input())
for _ in range(m):
    a, b = map(int, input().split())
    print(grid[a - 1][b - 1])
