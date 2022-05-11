"""
PyPy3로 제출
"""
import sys
from collections import deque

input = sys.stdin.readline


def bfs():
    queue = deque([(a, "")])
    visited[a] = True
    
    while queue:
        x, path = queue.popleft()
        
        if x == b:
            return path
        
        tmp = (x * 2) % MAX
        if not visited[tmp]:
            queue.append((tmp, path + "D"))
            visited[tmp] = True
        
        tmp = (x - 1) % MAX
        if not visited[tmp]:
            queue.append((tmp, path + "S"))
            visited[tmp] = True
        
        tmp = ((x * 10) + (x //1000)) % MAX
        if not visited[tmp]:
            queue.append((tmp, path + "L"))
            visited[tmp] = True

        tmp = ((x // 10) + (x % 10 * 1000)) % MAX
        if not visited[tmp]:
            queue.append((tmp, path + "R"))
            visited[tmp] = True

                
MAX = 10000
T = int(input())
for _ in range(T):
    visited = [False] * MAX
    a, b = map(int, input().split())
    print(bfs())
