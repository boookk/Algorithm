"""
치킨 거리는 집을 기준으로 정해지기 때문에 3중 for문으로 풀었다.
치킨 집을 기준으로 한다면, combinations 사용하지 않고 2중 for문으로도 해결 가능
"""
import sys
from itertools import combinations


input = sys.stdin.readline

n, m = map(int, input().split())

houses = list()
chicken = list()

for i in range(n):
    data = list(map(int, input().split()))
    for j in range(n):
        if data[j] == 1:
            houses.append((i, j))
        elif data[j] == 2:
            chicken.append((i, j))

answer = float('inf')
for ch in combinations(chicken, m):
    city_dist = 0
    for x, y in houses:
        chicken_dist = float('inf')
        for i in range(m):
            chicken_dist = min(chicken_dist, abs(ch[i][0] - x) + abs(ch[i][1] - y))
        city_dist += chicken_dist
    answer = min(answer, city_dist)

print(answer)
