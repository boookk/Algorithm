"""
DFS로 풀면서 시간 초과, 메모리 초과 문제가 발생하여 전역 변수, 딕셔너리, 집합 자료구조를 사용하기도 하였지만,
메모리 초과 문제를 해결할 수 없어서 BFS로 바꾸어 풀었다.
"""
import sys
from collections import deque
input = sys.stdin.readline


def bfs(x, y, num):
    cnt = 1
    queue = deque([(x, y)])
    visited[x][y] = num
    
    while queue:
        y, x = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= n or ny < 0 or ny >= m or visited[nx][ny] or not grid[nx][ny]:
                continue
            
            visited[nx][ny] = num
            queue.append((nx, ny))
            cnt += 1

    return cnt



n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
visited = [[0] * m for _ in range(n)]

group_cnt = dict()
answer = 0
group_idx = 0

for i in range(n):
    for j in range(m):
        if not visited[i][j] and grid[i][j]:
            group_idx += 1
            group_cnt[group_idx] = bfs(i, j, group_idx)
            

for i in range(n):
    for j in range(m):
        if not grid[i][j]:
            area = 1
            group_check = set()
            
            for d in range(4):
                nx = i + dx[d]
                ny = j + dy[d]
                
                if nx < 0 or nx >= n or ny < 0 or ny >= m or not visited[nx][ny]:
                    continue
                
                group_check.add(visited[nx][ny])
            
            for group_num in group_check:
                area += group_cnt[group_num]
                
            answer = max(answer, area)

print(answer)
