import sys
import heapq
input = sys.stdin.readline


n = int(input())
cards = [int(input()) for _ in range(n)]

heapq.heapify(cards)

answer = 0

for _ in range(n - 1):
    tmp = heapq.heappop(cards) + heapq.heappop(cards)
    answer += tmp
    heapq.heappush(cards, tmp)

print(answer)
