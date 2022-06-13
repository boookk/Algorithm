import sys

input = sys.stdin.readline

w, h = map(int, input().split())
odd = [0] * h
even = [0] * h

for i in range(w):
    n = int(input())
    if i % 2:   # 종유석
        odd[n - 1] += 1
    else:
        even[n - 1] += 1

for i in range(h - 1, 0, -1):
    odd[i - 1] += odd[i]
    even[i - 1] += even[i]

m = w
ans = 0

for i in range(h):
    tmp = even[i] + odd[h - 1 - i]
    if tmp < m:
        m = tmp
        ans = 1
    elif tmp == m:
        ans += 1
    
print(m, end=' ')
print(ans)
