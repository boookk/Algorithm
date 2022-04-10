"""
해당 문제는 그래프탐색과 더불어 분리집합으로 분류가 되어 있어서 분리집합 알고리즘을 적용하였다.
마지막에 결과를 판별할 때, 같은 집합에 속한다면(= 여행이 가능한 경로) 노드들의 부모가 같다.
중복을 없애고 봤을 때, 길이가 1이라면 YES를 출력한다.
"""
import sys


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


input = sys.stdin.readline
n = int(input())
m = int(input())

parent = [i for i in range(n + 1)]

for i in range(1, n + 1):
    graph = list(map(int, input().split()))
    for j in range(i, n + 1):
        if graph[j - 1]:
            union(i, j)

plan = list(map(int, input().split()))
result = []
for p in plan:
    result.append(find(p))

print("YES" if len(set(result)) == 1 else "NO")
