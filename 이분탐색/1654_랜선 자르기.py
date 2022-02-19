"""
line 18의 if문을 for문 안에 쓰는 바람에 계속 틀렸다고 떴었다.
실수하지 맙시다 😂
"""
import sys

k, n = map(int, sys.stdin.readline().split())
arr = [int(sys.stdin.readline()) for _ in range(k)]
start = 1
end = max(arr)

result = 0
while start <= end:
    mid = (start + end) // 2
    total = 0
    for a in arr:
        total += a // mid
    if total < n:
        end = mid - 1
    else:
        start = mid + 1
        result = mid
print(result)
