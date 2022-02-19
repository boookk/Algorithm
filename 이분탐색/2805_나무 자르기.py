"""
시간 초과가 계속 발생해서 line 10에서 max함수대신 정렬한 리스트의 마지막 요소를 대입하고 line 15에서 리스트 컴프리헨션을 사용해서 해결했다.
"""
import sys

n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()
start = 1
end = arr[-1]

result = 0
while start <= end:
    mid = (start + end) // 2
    total = sum([a - mid for a in arr if a > mid])
    if total < m:
        end = mid - 1
    else:
        start = mid + 1
        result = mid
print(result)
