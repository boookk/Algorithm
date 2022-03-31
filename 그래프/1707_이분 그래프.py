"""
좀 많이 힘들게 풀었다.. 출력 초과, 시간 초과, 최대 재귀 횟수 초과 ...
sys 라이브러리를 사용하여 입력받고 sys.setrecursionlimit(10**6) 부분으로 최대 재귀호출할 수 있는 수를 늘려서 해결했지만,
너무 찝찝한 느낌이 들어서 BFS로 다시 풀었다.
훨씬 깔끔해진 느낌이다 😊
"""


"""
DFS 풀이
"""

import sys
sys.setrecursionlimit(10**6)


def dfs(v, group):
    visited[v] = group

    for i in graph[v]:
        if visited[i] == visited[v]:
            return False
        if not visited[i]:
            if not dfs(i, -group):
                return False

    return True


K = int(input())
for _ in range(K):
    flag = True
    v, e = map(int, sys.stdin.readline().split())
    visited = [0] * (v + 1)
    graph = [[] for _ in range(v + 1)]
    for _ in range(e):
        i, j = map(int, sys.stdin.readline().split())
        graph[i].append(j)
        graph[j].append(i)

    for i in range(1, v+1):
        if not visited[i]:
            if not dfs(i, 1):
                flag = False
                break

    if flag:
        print("YES")
    else:
        print("NO")
        
   
  
  
"""
BFS 풀이
"""
import sys
from collections import deque


def bfs(v):
    # 정점 1의 그룹을 1로 설정
    queue = deque([v])
    visited[v] = 1

    while queue:
        v = queue.popleft()

        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = -visited[v]
            if visited[i] == visited[v]:
                return False

    return True


K = int(input())
for _ in range(K):
    flag = True
    v, e = map(int, sys.stdin.readline().split())
    visited = [0] * (v + 1)
    graph = [[] for _ in range(v + 1)]
    for _ in range(e):
        i, j = map(int, sys.stdin.readline().split())
        graph[i].append(j)
        graph[j].append(i)

    for i in range(1, v + 1):
        if visited[i] == 0:
            if not bfs(i):
                flag = False
                break

    print("YES" if flag else "NO")
