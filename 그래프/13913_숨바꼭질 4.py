"""
경로를 출력해주기 위해 리스트 move를 선언하여 해당 위치에 해당 위치로 오기 전의 위치를 저장한다.
이후 k부터 역으로 경로를 찾을 수 있다.
"""
import sys
from collections import deque


def bfs():
    queue = deque([n])
    visited[n] = 0

    while queue:
        x = queue.popleft()

        if x == k:
            break

        for op in [x * 2, x - 1, x + 1]:
            if 0 <= op < MAX and visited[op] == -1:
                visited[op] = visited[x] + 1
                move[op] = x
                queue.append(op)


input = sys.stdin.readline
n, k = map(int, input().split())
MAX = 100001
visited = [-1] * MAX
move = [-1] * MAX

bfs()

result = [k]
for _ in range(visited[k]):
    result.append(move[result[-1]])

print(visited[k])
print(*result[::-1])
