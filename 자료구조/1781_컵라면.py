import sys
import heapq
input = sys.stdin.readline


n = int(input())
info = [list(map(int, input().split())) for _ in range(n)]

heap = list()

info.sort()

for t, c in info:
    heapq.heappush(heap, c)
    
    if t < len(heap):
        heapq.heappop(heap)

print(sum(heap))
