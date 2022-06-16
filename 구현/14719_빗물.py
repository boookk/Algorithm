import sys


input = sys.stdin.readline

h, w = map(int, input().split())
brick = list(map(int, input().split()))

ans = 0
for i in range(1, w - 1):
    left = max(brick[:i])
    right = max(brick[i + 1:])
    
    m = min(left, right)
    
    if brick[i] < m:
        ans += m - brick[i]
        
print(ans)
