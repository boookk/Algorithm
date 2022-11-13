import sys
import heapq
input = sys.stdin.readline


n = int(input())
lectures = [tuple(map(int, input().split())) for _ in range(n)]

lectures.sort(key=lambda x: x[1])

heap = list()

for pay, day in lectures:
    heapq.heappush(heap, pay)
    
    if len(heap) > day:
        heapq.heappop(heap)

print(sum(heap))
