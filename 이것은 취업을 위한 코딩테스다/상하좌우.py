""" 구현 """
n = int(input())
direction = input().split()

x = 1
y = 1
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
step = {'L': 0, 'R' : 1, 'U': 2, 'D': 3}

for d in direction:
    nx = x + dx[step[d]]
    ny = y + dy[step[d]]

    if 0 < nx <= n and 0 < ny <= n:
        x, y = nx, ny

print(x, y)
