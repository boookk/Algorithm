import sys
sys.stdin = open("data.txt", 'r')
input = sys.stdin.readline


n = int(input())
train = list(map(int, input().split()))
max_car = int(input())

ps = [0]
val = 0
for t in train:
    val += t
    ps.append(val)

dp = [[0] * (n + 1) for _ in range(4)]

for i in range(1, 4):
    for j in range(i * max_car, n + 1):
        if i == 1:
            dp[i][j] = max(dp[i][j - 1], ps[j] - ps[j - max_car])
        else:
            dp[i][j] = max(dp[i][j - 1], dp[i - 1][j - max_car] + ps[j] - ps[j - max_car])

print(dp[3][n])
