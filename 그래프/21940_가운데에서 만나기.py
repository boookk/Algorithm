"""
1 ~ n + 1의 범위를 0 ~ n으로 바꾸고 나서 출력할 때 그 범위를 원상복구하지 않아 계속 틀렸다..
"""
import sys
input = sys.stdin.readline
INF = float('inf')

N,M = map(int,input().split())
graph = [[0 if x == y else INF for y in range(N + 1)] for x in range(N + 1)]

for _ in range(M):
    a, b, t = map(int,input().split())
    graph[a][b] = min(graph[a][b], t)

for mid in range(1, N + 1):
    for end in range(1, N + 1):
        for start in range(1, N + 1):
            if graph[start][end] > graph[start][mid] + graph[mid][end]:
                graph[start][end] = graph[start][mid] + graph[mid][end]

K = int(input())
friend_list = list(map(int,input().split()))
min_value = INF
min_list = []
for city in range(1, N + 1):
    temp_max = 0
    for p_num in friend_list:
        if graph[p_num][city] + graph[city][p_num] > temp_max:
            temp_max = graph[p_num][city] + graph[city][p_num]

    if temp_max < min_value:
        min_value = temp_max
        min_list = [city]
    elif temp_max == min_value:
        min_list.append(city)

print(*min_list)
