import sys
import heapq
input = sys.stdin.readline


n = int(input())

left_heap = list()
right_heap = list()

for _ in range(n):
    num = int(input())
    
    if len(left_heap) == len(right_heap):
        heapq.heappush(left_heap, -num)
    else:
        heapq.heappush(right_heap, num)
    
    if right_heap and right_heap[0] < -left_heap[0]:
        left_val = heapq.heappop(left_heap)
        right_val = heapq.heappop(right_heap)
        
        heapq.heappush(left_heap, -right_val)
        heapq.heappush(right_heap, -left_val)
    
    print(-left_heap[0])
