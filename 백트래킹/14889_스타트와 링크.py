"""
DFS로 풀려고 했으나, 팀을 0과 1로 나누다 보니 이전과 똑같이 나눠지는 경우를 처리하지 못하여 계속 시간 초과가 발생하였다.
결국 itertools.combinations를 사용하여 문제를 해결했다.
팀이 나눠지는 경우의 경우의 조합을 구하여 리스트에 저장하고, 
그 후 i번째 인덱스와 -i-1번째 인덱스 각각을 다른 팀으로 취급하여 능력치의 차이를 구했다.
"""


""" 첫 번째 풀이 (DFS)"""
import sys


def dfs(count):
    global result
    if n // 2 == count:
        start = 0
        link = 0
        for i in range(n):
            for j in range(n):
                if visited[i] == visited[j] == 1:
                    start += graph[i][j]
                elif visited[i] == visited[j] == 0:
                    link += graph[i][j]
        result = min(result, abs(start - link))

    for i in range(count, n):
        if visited[i]:
            continue
        visited[i] = 1
        dfs(count + 1)
        visited[i] = 0


n = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
visited = [0] * n
result = 100
dfs(0)
print(result)


""" 두 번째 풀이 (조합 이용) """
import sys
from itertools import combinations

n = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
combination = list(combinations(range(n), n // 2))
result = 100

for i in range(len(combination) // 2):
    start = 0
    for j in combination[i]:
        for k in combination[i]:
            start += graph[j][k]

    link = 0
    for j in combination[-i-1]:
        for k in combination[-i-1]:
            link += graph[j][k]

    result = min(result, abs(start - link))

print(result)
