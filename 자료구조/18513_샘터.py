import sys
from collections import deque
input = sys.stdin.readline


n, k = map(int, input().split())
houses = list(map(int, input().split()))

answer = 0
visited = set()
queue = deque()

for loc in houses:
    queue.append((loc, 1))
    visited.add(loc)

while queue:
    x, dist = queue.popleft()
    
    for nx in [x - 1, x + 1]:
        if nx in visited:
            continue
        
        visited.add(nx)
        answer += dist
        k -= 1
        queue.append((nx, dist + 1))
        
        if not k:
            queue.clear()
            break

print(answer)
