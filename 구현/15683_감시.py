import sys
import copy


def watch(maps, direction, x, y):
    for d in direction:
        nx, ny = x, y
        while True:
            nx += dx[d]
            ny += dy[d]
            if nx < 0 or nx >= n or ny < 0 or ny >= m or maps[nx][ny] == 6:
                break
            if maps[nx][ny] == 0:
                maps[nx][ny] = 7


def dfs(lst, cnt):
    global ans
    
    if cnt == len(cctv):
        val = 0
        for row in lst:
            val += row.count(0)
        ans = min(ans, val)
        return
        
    tmp = copy.deepcopy(lst)
    cctv_num, x, y =  cctv[cnt]
    for d in D[cctv_num]:
        watch(tmp, d, x, y)
        dfs(tmp, cnt + 1)
        tmp = copy.deepcopy(lst)


input = sys.stdin.readline

n, m = map(int, input().split())

graph = []
cctv = []
for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(m):
        if 1 <= graph[i][j] <= 5:
            cctv.append((graph[i][j], i, j))

dx = [-1, 0, 1, 0]  # 위, 왼쪽, 아래, 오른쪽
dy = [0, -1, 0, 1]
D = [[], 
     [[0], [1], [2], [3]],
     [[0, 2], [1, 3]],
     [[0, 1], [0, 3], [1, 2], [2, 3]],
     [[0, 1, 2], [0, 1, 3], [0, 2, 3], [1, 2, 3]], 
     [[0, 1, 2, 3]]]

ans = float('inf')
dfs(graph, 0)
print(ans)
