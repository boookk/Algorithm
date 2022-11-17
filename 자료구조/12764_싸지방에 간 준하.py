"""
PyPy3 제출
"""
import sys
import heapq
input = sys.stdin.readline

n = int(input())
times = [tuple(map(int, input().split())) for _ in range(n)]

heapq.heapify(times)

end_time = [0] * n
answer = [0] * n
count = 0

while times:
    start, end = heapq.heappop(times)
    for i in range(n):
        if end_time[i] <= start:
            if end_time[i] == 0:
                count += 1
            end_time[i] = end
            answer[i] += 1
            break

print(count)
print(*answer[:count])
