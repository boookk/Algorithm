import sys
from collections import deque


input = sys.stdin.readline

n, k = map(int, input().split())
belt = deque(list(map(int, input().split())))
robot = deque([0] * n)

step = 1

while True:
    belt.rotate(1)
    robot.rotate(1)
    robot[-1] = 0

    for i in range(n - 2, -1, -1):
        if robot[i] and not robot[i + 1] and belt[i + 1]:
            robot[i] = 0
            robot[i + 1] = 1
            belt[i + 1] -= 1
    robot[-1] = 0

    if not robot[0] and belt[0]:
        robot[0] = 1
        belt[0] -= 1
    if belt.count(0) >= k:
        break
    step += 1

print(step)
