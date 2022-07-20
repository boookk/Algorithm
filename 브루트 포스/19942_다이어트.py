import sys


def dfs(idx, composition, sum_nutrient):
    global min_cost, answer
    
    if sum_nutrient[4] >= min_cost:
        return
    
    if sum_nutrient[0] >= mp and sum_nutrient[1] >= mf and sum_nutrient[2] >= ms and sum_nutrient[3] >= mv:
        min_cost = sum_nutrient[4]
        answer = composition.copy()
        return
    
    if idx >= n:
        return
    
    for i in range(5):
        sum_nutrient[i] += nutrient[idx][i]
    composition.append(idx + 1)
    dfs(idx + 1, composition, sum_nutrient)
    
    for i in range(5):
        sum_nutrient[i] -= nutrient[idx][i]
    composition.pop()
    dfs(idx + 1, composition, sum_nutrient)


input = sys.stdin.readline

n = int(input())
mp, mf, ms, mv = map(int, input().split())
nutrient = [list(map(int, input().split())) for _ in range(n)]

min_cost = float('inf')
answer = []

dfs(0, [], [0, 0, 0, 0, 0])
if min_cost == float('inf'):
    print(-1)
else:
    print(min_cost)
    print(*answer)
