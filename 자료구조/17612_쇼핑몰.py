import sys
import heapq
input = sys.stdin.readline


n, k = map(int, input().split())

counter = list()
after = list()
counterIdx = 1
answer = 0

for _ in range(n):
    id, w = map(int, input().split())
    
    if counterIdx <= k:
        heapq.heappush(counter, (w, counterIdx, id))
        counterIdx += 1
    else:
        time_, counterIdx_, id_ = heapq.heappop(counter)
        heapq.heappush(after, (time_, -counterIdx_, id_))
        heapq.heappush(counter, (time_ + w, counterIdx_, id))

while counter:
    time_, counterIdx_, id_ = heapq.heappop(counter)
    heapq.heappush(after, (time_, -counterIdx_, id_))

for i in range(1, len(after) + 1):
    _, _, id = heapq.heappop(after)
    answer += i * id

print(answer)
