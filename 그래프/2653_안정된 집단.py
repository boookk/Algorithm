"""
그래프 이론 중 탐색 문제가 아니라, 구현 문제였다.
범위가 크지 않았기 때문에 각자의 기준에서 서로 좋아하는 집단인지 비교를 하여 문제를 해결했다.
"""
import sys
input = sys.stdin.readline


def getGroup(x):
    group_ = list()

    for y in range(1, n + 1):
        if grid[x][y] == 0:
            group_.append(y)

    return group_


n = int(input())
grid = [[0] * (n + 1)] + [[0] + list(map(int, input().split())) for _ in range(n)]

visited = [False] * (n + 1)
ans = list()
for i in range(1, n + 1):

    if not visited[i]:
        group = getGroup(i)

        if len(group) == 1:
            print(0)
            exit(0)

        for g in group:
            if i == g:
                continue
            if group == getGroup(g):
                visited[g] = True
            else:
                print(0)
                exit(0)

        ans.append(group)

print(len(ans))
for a in ans:
    print(*a)
