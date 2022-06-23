import sys


def tumble(direction):
    a, b, c, d, e, f = dice[0], dice[1], dice[2], dice[3], dice[4], dice[5]
    if direction == 1:      # 동
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = [d, b, a, f, e, c]
    elif direction == 2:    # 서
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = [c, b, f, a, e, d]
    elif direction == 3:    # 북
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = [e, a, c, d, f, b]
    else:                   # 남
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = [b, f, c, d, a, e]


input = sys.stdin.readline

n, m, x, y, k = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]
commands = list(map(int, input().split()))

dice = [0] * 6

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

for command in commands:
    nx = x + dx[command - 1]
    ny = y + dy[command - 1]
    
    if nx < 0 or nx >= n or ny < 0 or ny >= m:
        continue
    
    tumble(command)
    
    if maps[nx][ny]:
        dice[5] = maps[nx][ny]
        maps[nx][ny] = 0
    else:
        maps[nx][ny] = dice[5]
    
    x, y = nx, ny
    print(dice[0])
