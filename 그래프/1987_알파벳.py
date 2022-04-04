"""
중복된 알파벳을 선택하지 않기 위해 리스트 alpha를 만들어 방문 여부를 체크한다.
"""

import sys


def dfs(x, y, count):
    global ans

    ans = max(ans, count)

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx <= -1 or nx >= r or ny <= -1 or ny >= c or alpha[arr[nx][ny]]:
            continue

        alpha[arr[nx][ny]] = 1
        dfs(nx, ny, count + 1)
        alpha[arr[nx][ny]] = 0


input = sys.stdin.readline

r, c = map(int, input().split())
arr = [list(map(lambda x: ord(x) - 65, input().rstrip())) for _ in range(r)]
alpha = [0] * 26
alpha[arr[0][0]] = 1
ans = 0

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

dfs(0, 0, 1)

print(ans)
