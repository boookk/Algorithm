import sys
input = sys.stdin.readline


n = int(input())
reports = [tuple(map(int, input().split())) for _ in range(n)]

reports.sort(key=lambda x: -x[1])

answer = 0
visited = [False] * 1001

for d, w in reports:
    while d > 0 and visited[d]:
        d -= 1
    if d:
        visited[d] = True
        answer += w

print(answer)
