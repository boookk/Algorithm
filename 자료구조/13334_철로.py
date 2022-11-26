import sys
import heapq
input = sys.stdin.readline


n = int(input())
info = [list(map(int, input().split())) for _ in range(n)]
d = int(input())

answer = 0
heap = list()
tmp = list()

for house, office in info:
    if abs(house - office) <= d:
        tmp.append(sorted([house, office]))

tmp.sort(key=lambda x: x[1])

for road in tmp:
    while heap and heap[0][0] < road[1] - d:
        heapq.heappop(heap)
    heapq.heappush(heap, road)
    answer = max(answer, len(heap))

print(answer)
