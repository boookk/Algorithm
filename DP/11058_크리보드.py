"""
복붙을 세 번까지 정한 이유
1. A의 개수가 6개일 때까지는 A를 출력하는 편이 유리하다.
2. 7번째 비교할 때 복붙을 최대 세 번할 경우까지 비교 가능하다.
"""
import sys

input = sys.stdin.readline

n = int(input())
dp = [i for i in range(n + 1)]

for i in range(7, n + 1):
    dp[i] = max(dp[i - 3] * 2, dp[i - 4] * 3, dp[i - 5] * 4)    # 복붙 한 번, 두 번, 세 번
    
print(dp[n])
