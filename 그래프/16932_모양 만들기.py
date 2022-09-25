"""
DFS로 풀면서 시간 초과, 메모리 초과 문제가 발생하여 전역 변수, 딕셔너리, 집합 자료구조를 사용하기도 하였지만,
메모리 초과 문제를 해결할 수 없어서 BFS로 바꾸어 풀었다.
++++ 원인은 재귀 최대 깊이 설정이었다... sys.setrecursionlimit(10 ** 8) 로 고정해두었기 때문에 메모리 초과가 발생한 것이었다.
재귀 최대 깊이 설정을 제거한 것부터 10 ** 5, 10 ** 6까지 실험해 보면서 10 ** 5 보다는 크고 10 ** 6 보다는 작게 설정해야하는 것을 알 수 있었다.
"""

##############
## BFS
#############
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


#################
## DFS 
################
import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline


def dfs(x, y, cnt):
    ans = 1
    
    visited[x][y] = cnt
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if nx < 0 or nx >= n or ny < 0 or ny >= m or visited[nx][ny] or not grid[nx][ny]:
            continue
    
        ans += dfs(nx, ny, cnt)
    
    return ans


n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
visited = [[0] * m for _ in range(n)]
group_cnt = [0]
answer = 0
cnt = 0

for i in range(n):
    for j in range(m):
        if not visited[i][j] and grid[i][j]:
            cnt += 1
            group_cnt.append(dfs(i, j, cnt))
            

for i in range(n):
    for j in range(m):
        if not grid[i][j]:
            area = 1
            group_check = set()
            
            for d in range(4):
                nx = i + dx[d]
                ny = j + dy[d]
                
                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    continue
                
                group_num = visited[nx][ny]
                if not group_num or group_num in group_check:
                    continue
                
                area += group_cnt[group_num]
                group_check.add(group_num)
                
            answer = max(answer, area)

print(answer)
