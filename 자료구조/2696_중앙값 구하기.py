import sys
import heapq
input = sys.stdin.readline


T = int(input())
for _ in range(T):
    n = int(input())
    
    arr = list()
    left_heap = list()
    right_heap = list()
    
    bounds = n // 10 + (n % 10 != 0)
    for i in range(bounds):
        arr += list(map(int, input().split()))
    
    mid = arr[0]
    answer = [mid]
    
    for idx, val in enumerate(arr[1:], 1):
        if val > mid:
            heapq.heappush(right_heap, val)
        else:
            heapq.heappush(left_heap, -val)
        
        if idx % 2 == 0:
            if len(left_heap) < len(right_heap):
                heapq.heappush(left_heap, -mid)
                mid = heapq.heappop(right_heap)
            elif len(left_heap) > len(right_heap):
                heapq.heappush(right_heap, mid)
                mid = -heapq.heappop(left_heap)
            answer.append(mid)
    
    print(len(answer))
    
    for i in range(0, len(answer), 10):
        print(*answer[i:i + 10])
