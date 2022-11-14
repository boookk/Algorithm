import sys
import heapq
input = sys.stdin.readline


n = int(input())
stations = [tuple(map(int, input().split())) for _ in range(n)]
L, P = map(int, input().split())

answer = 0
heap = list()

heapq.heapify(stations)

while P < L:
    while stations and stations[0][0] <= P:
        dist, fuel = heapq.heappop(stations)
        heapq.heappush(heap, [-fuel, dist])
    
    if not heap:
        answer = -1
        break
    
    fuel, dist = heapq.heappop(heap)
    P += -fuel
    answer += 1

print(answer)
