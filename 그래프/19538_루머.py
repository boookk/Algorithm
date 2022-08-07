import sys
from collections import deque


def bfs():
    queue = deque(spreader)
    turn = [0] * (n + 1)

    for i in range(1, n + 1):
        turn[i] = len(people_around[i]) // 2

    while queue:
        person = queue.popleft()

        for p in people_around[person]:
            turn[p] -= 1
            
            if p == 0:
                break

            if start_time[p] == -1 and turn[p] <= 0:
                start_time[p] = start_time[person] + 1
                queue.append(p)


input = sys.stdin.readline

n = int(input())
people_around = [[]] + [list(map(int, input().split())) for _ in range(n)]

m = int(input())
spreader = list(map(int, input().split()))

start_time = [-1] * (n + 1)
for i in range(m):
    start_time[spreader[i]] = 0

bfs()
print(*start_time[1:])
