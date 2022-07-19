import sys
from itertools import combinations


def dfs(cnt):
    global result
    
    if cnt == 15:
        result = 1
        for contry in scores:
            if contry.count(0) != 3:
                result = 0
                break
        return

    team1, team2 = games[cnt]
    for a, b in ((0, 2), (1, 1), (2, 0)):
        if scores[team1][a] > 0 and scores[team2][b] > 0:
            scores[team1][a] -= 1
            scores[team2][b] -= 1
            dfs(cnt + 1)
            scores[team1][a] += 1
            scores[team2][b] += 1


sys.stdin = open('data.txt', 'r')
input = sys.stdin.readline

answer = []
games = list(combinations(range(6), 2))

for _ in range(4):
    tmp = list(map(int, input().split()))
    scores = [tmp[i:i + 3] for i in range(0, 16, 3)]
    result = 0
    dfs(0)
    answer.append(result)

print(*answer)
