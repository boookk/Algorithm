"""
루트 노드와 자식 노드 하나가 있을 때, 자식 노드를 지우면 루트 노드만 남게 되는 경우가 있다.
이 때 리프노드는 1이어야 한다.
리프 노드는 자식 노드의 개수가 0인 것으로 루트 노드가 자식을 갖고 있지 않기 때문이다.
이것을 고려하지 못해 틀렸었다..
"""
import sys


def dfs(x):
    global ans
    if not graph[x]:
        ans += 1
        return

    for i in graph[x]:
        if i != del_node:
            dfs(i)
        else:
            if len(graph[x]) == 1:
                ans += 1


input = sys.stdin.readline
n = int(input())
graph = [[] for _ in range(n)]
parent = list(map(int, input().split()))
ans = 0
root = -1

for i in range(n):
    if parent[i] == -1:
        root = i
    else:
        graph[parent[i]].append(i)

del_node = int(input())
if del_node == root:
    print(0)
else:
    dfs(root)
    print(ans)
