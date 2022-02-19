"""
시간 초과가 발생해서 PyPy3로 성공했다.
"""
n, c = map(int, input().split())
locations = [int(input()) for _ in range(n)]
locations.sort()
start = 1
end = locations[-1] - locations[0]      # 공유기 사이의 최대 거리로 가정

result = 0
while start <= end:
    mid = (start + end) // 2
    count = 1
    current = locations[0]
    for i in range(1, n):
        if current + mid <= locations[i]:
            count += 1
            current = locations[i]
    if count < c:
        end = mid - 1
    else:
        start = mid + 1
        result = mid
print(result)
