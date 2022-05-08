"""
루트노드가 공통 부모가 될 경우, 루트노드에는 0이라는 원소가 있고 parent 리스트의 0번째 원소에는 0이 저장되어 있다.
0일 경우를 고려하여 문제를 풀어야 한다.
내가 처음에 구현한 알고리즘은 이를 고려하지 못하여 0이라는 값을 출력하였다.
"""
import sys
from collections import deque

input = sys.stdin.readline


def bfs():
    visited = [False] * (n + 1)
    queue = deque([target_a, target_b])
    visited[target_a] = True
    visited[target_b] = True

    while queue:
        x = queue.popleft()

        if not graph[x]:
            continue

        if visited[graph[x]]:
            print(graph[x])
            return

        visited[graph[x]] = True
        queue.append(graph[x])


T = int(input())
for _ in range(T):
    n = int(input())
    graph = [0] * (n + 1)

    for _ in range(n - 1):
        a, b = map(int,  input().split())
        graph[b] = a

    target_a, target_b = map(int, input().split())

    bfs()
