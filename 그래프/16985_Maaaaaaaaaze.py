import sys
from collections import deque
from itertools import permutations
input = sys.stdin.readline
INF = sys.maxsize


def stack_board(order, idx):
    if answer == 12:
        return
    if idx == 5:
        bfs(order)
        return
    for _ in range(4):
        board_rotate(order[idx])
        stack_board(order, idx + 1)


def board_rotate(idx):
    rotated = list(zip(*board[idx][::-1]))
    for i in range(5):
        board[idx][i] = list(rotated[i])


def bfs(order):
    global answer, visited_num
    
    dx = [-1, 1, 0, 0, 0, 0]
    dy = [0, 0, -1, 0, 1, 0]
    dz = [0 ,0, 0, -1, 0, 1]
    
    new_board = [board[idx] for idx in order]

    if new_board[0][0][0] != 1 or new_board[4][4][4] != 1:
        return
    
    visited_num += 1
    
    queue = deque([(0, 0, 0, 0)])
    visited[0][0][0] = visited_num
    
    while queue:
        x, y, z, cnt = queue.popleft()
        
        if cnt >= answer:
            continue
        
        if x == y == z == 4:
            answer = min(answer, cnt)
            break
        
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
        
            if nx < 0 or nx >= 5 or ny < 0 or ny >= 5 or nz < 0 or nz >= 5 or not new_board[nx][ny][nz] or visited[nx][ny][nz] == visited_num:
                continue
            
            visited[nx][ny][nz] = visited_num
            queue.append((nx, ny, nz, cnt + 1))


board = [[list(map(int, input().split())) for _ in range(5)] for _ in range(5)]
visited = [[[0] * 5 for _ in range(5)] for _ in range(5)]

answer = INF
visited_num = 0

for order in permutations(range(5)):
    stack_board(order, 0)
print(-1 if answer == INF else answer)
