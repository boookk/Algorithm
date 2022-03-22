"""
우선, 덱을 사용하여 건물을 짓는 순서를 찾지 않아도 된다.
- cmd가 1이라면, 해당 번호의 건물의 진입 차수를 확인하고 진입 차수가 0이라면 건물의 개수를 증가시킨다.
그 후 해당 번호의 건물의 개수가 1이라면, 다음으로 지을 수 있는 건물들의 진입 차수를 감소시킨다.
- cmd가 1이고 진입 차수가 0이 아니라면, 종료시킨다.

- cmd가 2라면, 해당 번호의 건물이 존재하는지 여부를 판단하여 지어진 건물이 없다면 종료시키면 된다.
- 건물이 존재한다면, 해당 건물의 개수를 감소시키고, 건물이 존재하지 않게 되면, 해당 번호 다음으로 지을 수 있는 건물들의 진입 차수를 증가시킨다.
"""

import sys

input = sys.stdin.readline

n, m, k = map(int, input().split())     # 건물 종류의 수, 건물 관계의 개수, 게임 정보의 개수
graph = [[] for _ in range(n + 1)]
inDegree = [0] * (n + 1)
building = [0] * (n + 1)
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    inDegree[y] += 1


for _ in range(k):
    cmd, num = map(int, input().split())

    if cmd == 1:
        if inDegree[num]:
            print('Lier!')
            exit(0)
        building[num] += 1
        if building[num] == 1:
            for i in graph[num]:
                inDegree[i] -= 1
    else:
        if building[num] == 0:
            print('Lier!')
            exit(0)
        building[num] -= 1
        if not building[num]:
            for i in graph[num]:
                inDegree[i] += 1

print('King-God-Emperor')
