"""
PyPy3 제출
"""
import sys
from collections import deque
input = sys.stdin.readline


n, m, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

answer = 0
dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]
trees = [[deque() for _ in range(n)] for _ in range(n)]
grid = [[5] * n for _ in range(n)]

for _ in range(m):
    x, y, z = map(int, input().split())
    trees[x - 1][y - 1].append(z)

for _ in range(k):
    dead_trees = deque()
    
    for x in range(n):
        for y in range(n):
            for z in range(len(trees[x][y])):
                if trees[x][y][z] <= grid[x][y]:    # 봄
                    grid[x][y] -= trees[x][y][z]
                    trees[x][y][z] += 1
                else:                               # 여름
                    for _ in range(z, len(trees[x][y])):
                        grid[x][y] += trees[x][y].pop() // 2
                    break
    
    for x in range(n):
        for y in range(n):
            for z in range(len(trees[x][y])):       # 가을
                if trees[x][y][z] % 5 == 0:
                    for i in range(8):
                        nx = x + dx[i]
                        ny = y + dy[i]
                        
                        if nx < 0 or nx >= n or ny < 0 or ny >= n:
                            continue
                        
                        trees[nx][ny].appendleft(1)
            
            grid[x][y] += board[x][y]               # 겨울

for i in range(n):
    for j in range(n):
        answer += len(trees[i][j])

print(answer)
