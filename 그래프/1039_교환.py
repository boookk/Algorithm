import sys
from collections import deque
input = sys.stdin.readline


def bfs():
    global ans
    
    visited = set((n, 0))
    queue = deque([(n, 0)])
    
    while queue:
        num, cnt = queue.popleft()
        
        if cnt == k:
            ans = max(ans, num)
            continue
        
        num = list(str(num))
        for i in range(m):
            for j in range(i + 1, m):
                if i == 0 and num[j] == '0':
                    continue
                num[i], num[j] = num[j], num[i]
                tmp = int(''.join(num))
                if (tmp, cnt + 1) not in visited:
                    queue.append((tmp, cnt + 1))
                    visited.add((tmp, cnt + 1))
                num[i], num[j] = num[j], num[i]   


n, k = map(int, input().split())
m = len(str(n))

ans = 0
bfs()
print(ans if ans else -1)
