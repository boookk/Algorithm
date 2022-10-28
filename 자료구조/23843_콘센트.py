import heapq

n, m = map(int, input().split())
times = sorted(list(map(int, input().split())))

concent = [0] * m

while times:
    heapq.heappush(concent, heapq.heappop(concent) + times.pop())

print(max(concent))
