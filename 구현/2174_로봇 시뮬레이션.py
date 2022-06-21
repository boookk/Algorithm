import sys


input = sys.stdin.readline

D = {'N': 0, 'W': 1, 'S': 2, 'E': 3}
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

a, b = map(int, input().split())
n, m = map(int, input().split())

visited = [[0] * a for _ in range(b)]
robots = []
for i in range(1, n + 1):
    x, y, d = input().rstrip().split()  # x, y 좌표, 방향
    x, y = int(x) - 1, b - int(y)
    robots.append([y, x, D[d]])
    visited[y][x] = i

ans = 'OK'

for _ in range(m):
    robot, cmdType, cnt = input().rstrip().split()
    robot, cnt = int(robot), int(cnt)
    
    x, y, d = robots[robot - 1]
    if cmdType == 'L':
        d = (d + cnt) % 4
    elif cmdType == 'R':
        d = (d - cnt) % 4
    else:
        flag = True
        nx, ny = x, y
        for _ in range(cnt):
            nx += dx[d]
            ny += dy[d]
        
            if nx < 0 or nx >= b or ny < 0 or ny >= a:
                ans = f'Robot {robot} crashes into the wall'
                flag = False
                break
            
            if visited[nx][ny]:
                ans = f'Robot {robot} crashes into robot {visited[nx][ny]}'
                flag = False
                break
        
        if not flag:
            break
        
        visited[nx][ny] = robot
        visited[x][y] = 0
        x, y = nx, ny
        
    robots[robot - 1] = [x, y, d]

print(ans)
    
