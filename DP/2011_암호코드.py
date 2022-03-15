"""
* checkpoint
1. 입력받은 수가 0으로 시작하는지
2. 입력받은 수를 앞에서부터 탐색할 때 i 번째 수가 0이 아닌지
3. i - 1번째 수부터 i번째 수를 이었을 때 두 수가 이어는지
"""
import sys
input = sys.stdin.readline


x = '0' + input().rstrip()

if x[1] == '0':
    print('0')
    exit(0)

dp = [0] * len(x)
dp[0], dp[1] = 1, 1
for i in range(2, len(x)):
    num = int(x[i - 1:i + 1])

    if int(x[i]) > 0:
        dp[i] += dp[i - 1]
    if 10 <= num <= 26:
        dp[i] += dp[i - 2]

print(dp[-1] % 1000000)
