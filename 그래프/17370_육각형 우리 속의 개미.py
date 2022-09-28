"""
PyPy3 제출
다른 분들의 풀이를 보니 개선된 코드는 찾기 어려웠고, 규칙을 이용하여 결과값을 변수에 저장한 후 n에 해당하는 값을 출력했다.
"""
import sys
sys.setrecursionlimit(10 ** 5)
input = sys.stdin.readline


def dfs(cnt, d, x, y):
    global ans
    
    if cnt == n:
        if visited[x][y]:
            ans += 1
        return
    
    if visited[x][y]:
        return
    
    visited[x][y] = True
    
    for idx in dir[d]:
        dfs(cnt + 1, idx, x + dx[idx], y + dy[idx])
    
    visited[x][y] = False


n = int(input())

dx = [-1, -1, -1, 1, 1, 1]
dy = [0, -1, 1, 0, -1, 1]
dir = {0: (1, 2), 1: (0, 4), 2: (0, 5), 3: (4, 5), 4: (1, 3), 5: (2, 3)}
visited = [[False] * 50 for _ in range(50)]

ans = 0
visited[26][25] = True

dfs(0, 0, 25, 25)

print(ans)
