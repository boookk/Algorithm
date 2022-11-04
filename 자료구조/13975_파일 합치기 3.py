import sys
import heapq
input = sys.stdin.readline


T = int(input())
for _ in range(T):
    k = int(input())
    heap = list(map(int, input().split()))
    
    heapq.heapify(heap)
    
    answer = 0
    
    while len(heap) > 1:
        a = heapq.heappop(heap)
        b = heapq.heappop(heap)
        answer += a + b
        heapq.heappush(heap, a + b)
    
    print(answer)
