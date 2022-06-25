"""
PyPy3로 
"""
import sys


def spread():
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    
    tmp = [row[:] for row in graph]
    
    for x in range(r):
        for y in range(c):
            if graph[x][y] >= 5:
                spread_dust = 0
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    
                    if nx < 0 or nx >= r or ny < 0 or ny >= c or graph[nx][ny] == -1:
                        continue
                    
                    graph[nx][ny] += tmp[x][y] // 5
                    spread_dust += tmp[x][y] // 5

                graph[x][y] -= spread_dust


def up_purify():
    for i in range(air_cleaner[0] - 1, 0, -1): # 남쪽
        graph[i][0] = graph[i - 1][0]
    
    for i in range(c - 1):  # 서쪽
        graph[0][i] = graph[0][i + 1]
    
    for i in range(air_cleaner[0]):
        graph[i][c - 1] = graph[i + 1][c - 1]
    
    for i in range(c - 1, 1, -1):
        graph[air_cleaner[0]][i] = graph[air_cleaner[0]][i - 1]
    graph[air_cleaner[0]][1] = 0


def down_purify():
    for i in range(air_cleaner[1] + 1, r - 1):
        graph[i][0] = graph[i + 1][0]

    for i in range(c - 1):  # 서쪽
        graph[r - 1][i] = graph[r - 1][i + 1]
        
    for i in range(r - 1, air_cleaner[1], -1): # 남쪽
        graph[i][c - 1] = graph[i - 1][c - 1]
    
    for i in range(c - 1, 1, -1):
        graph[air_cleaner[1]][i] = graph[air_cleaner[1]][i - 1]
    graph[air_cleaner[1]][1] = 0


input = sys.stdin.readline

r, c, t = map(int, input().split())

air_cleaner = []
graph = []
for i in range(r):
    graph.append(list(map(int, input().split())))

    if graph[i][0] == -1:
        air_cleaner.append(i)

for _ in range(t):
    spread()
    up_purify()
    down_purify()

ans = 0
for row in graph:
    for val in row:
        if val > 0:
            ans += val

print(ans)
