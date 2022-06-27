import sys


input = sys.stdin.readline

n = int(input())

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

graph = [[0] * 101 for _ in range(101)]

for _ in range(n):
    x, y, d, g = map(int, input().split())  # 방향, 세대
    graph[y][x] = 1
    
    curve = [d]
    for _ in range(g):
        for i in range(len(curve) - 1, -1, -1):
            curve.append((curve[i] + 1) % 4)

    for c in curve:
        x += dx[c]
        y += dy[c]

        if x < 0 or x > 100 or y < 0 or y > 100:
            continue            
        graph[y][x] = 1

ans = 0
for i in range(100):
    for j in range(100):
        if graph[i][j] and graph[i + 1][j] and graph[i][j + 1] and graph[i + 1][j + 1]:
            ans += 1

print(ans)
