import sys
import heapq
input = sys.stdin.readline


n = int(input())
classes = [list(map(int, input().split())) for _ in range(n)]

classes.sort(key= lambda x: (x[1], x[2]))

rooms = [classes[0][2]]

for i in range(1, n):
    if classes[i][1] >= rooms[0]:
        heapq.heappop(rooms)
    heapq.heappush(rooms, classes[i][2])

print(len(rooms))
