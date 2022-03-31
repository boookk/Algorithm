"""
문제를 해결하면서 겪어던 3가지 이슈
1. 메모리 초과
  - 다익스트라 알고리즘으로 풀지 않아서 발생한 문제
  - 31번째 줄에 if문을 사용하여 문제 해결
2. 시간 초과
  - 우선순위 큐를 사용하는데, 우선순위 큐에 요소를 넣을 때 (노드번호, 비용) 순으로 넣어서 발생한 문제
  - python의 heapq는 첫 번째 요소를 기준으로 정렬된다.
  - 최단 거리를 구해야하기 위해서는 비용을 기준으로 정렬해야 하므로 (비용, 노드번호) 순으로 넣어야 한다.
3. 출력 불일치
  - 결과를 저장하는 리스트의 요소를 float('inf')로 초기화시키고 이를 그대로 출력하여 발생한 문제
  - 'inf'가 아닌 'INF'로 출력하도록 수정
"""

import sys
import heapq


def dijkstra():
    result = [float('inf')] * n
    result[start - 1] = 0

    heap = []
    heapq.heappush(heap, (0, start))

    while heap:
        dist, x = heapq.heappop(heap)

        for v, w in graph[x]:
            w += dist
            if result[v - 1] > w:
                heapq.heappush(heap, (w, v))
                result[v - 1] = w

    return result


input = sys.stdin.readline

n, m = map(int, input().split())
start = int(input())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append([v, w])

result = dijkstra()

for i in result:
    print(i if i != float('inf') else 'INF')
