"""
PyPy3로 제출.
저번에는 set()을 이용하여 스도쿠 문제를 풀어봤기 때문에 이번에는 다르게 풀어보았다.
"""
import sys


def dfs(idx):
    if idx == len(zeros):
        for i in range(9):
            print(*graph[i], sep='')
        exit(0)
    
    x, y = zeros[idx]
    
    for i in range(1, 10):       
        for j in range(9):
            nx = (j // 3) + 3 * (x // 3)
            ny = (j % 3) + 3 * (y // 3)
            if graph[j][y] == i or graph[x][j] == i or graph[nx][ny] == i:
                break
        else:
            graph[x][y] = i
            dfs(idx + 1)
            graph[x][y] = 0

input = sys.stdin.readline

graph = []
zeros = []
for i in range(9):
    graph.append(list(map(int, input().rstrip())))
    for j in range(9):
        if not graph[i][j]:
            zeros.append((i, j))

dfs(0)
