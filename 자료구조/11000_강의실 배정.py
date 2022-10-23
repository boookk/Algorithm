import sys
import heapq
input = sys.stdin.readline


n = int(input())
classes = [list(map(int, input().split())) for _ in range(n)]

classes.sort()

rooms = list()
heapq.heappush(rooms, classes[0][1])

for i in range(1, n):
    if classes[i][0] < rooms[0]:
        heapq.heappush(rooms, classes[i][1])
    else:
        heapq.heappop(rooms)
        heapq.heappush(rooms, classes[i][1])

print(len(rooms))
