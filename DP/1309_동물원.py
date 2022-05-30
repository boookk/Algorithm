"""
결과만 9901로 나누어 메모리 초과 발생.
중간 과정에서도 나머지를 저장해야 한다.
"""
import sys

input = sys.stdin.readline

n = int(input())
dp = [1, 3]

for i in range(2, n + 1):
    dp.append((dp[i - 1] * 2 + dp[i - 2]) % 9901)

print(dp[n])
