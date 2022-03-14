import sys
input = sys.stdin.readline


def find():
    answer = ''
    x, y = n, m
    while dp[x][y] != 0:
        if dp[x][y - 1] == dp[x][y] - 1 == dp[x - 1][y]:
            answer = str1[x - 1] + answer
            y -= 1
            x -= 1
        else:
            if dp[x - 1][y] > dp[x][y - 1]:
                x -= 1
            else:
                y -= 1
    return ''.join(answer)


str1 = input().rstrip()
str2 = input().rstrip()
n, m = len(str1), len(str2)
dp = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if str1[i - 1] == str2[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])

print(dp[n][m])
if dp[n][m] != 0:
    print(find())
