"""
이 문제에서 개미 전사는 최소한 한 칸 이상 떨어진 식량창고를 약탈할 수 있다.
첫 번째 풀이는 두 칸 이상 떨어진 경우를 고려하지 못했다.
두 칸 이상 떨어진 경우를 고려하기 위해 max()를 사용하여 이전에 계산했던 값과 비교하여 큰 값으로 dp 리스트를 갱신하였다.
"""

""" 첫 번째 풀이"""
n = int(input())
foods = list(map(int, input().split()))

dp = [0] * 4
dp[0] = foods[0]
dp[1] = foods[1]

for i in range(2, n):
    dp[i] = foods[i] + dp[i - 2]
print(dp[-1] if dp[-1] > dp[-2] else dp[-2])


""" 두 번째 풀이 """
n = int(input())
foods = list(map(int, input().split()))

dp = [0] * 4
dp[0] = foods[0]
dp[1] = max(foods[0], foods[1])

for i in range(2, n):
    dp[i] = max(dp[i - 1], dp[i - 2] + foods[i])

print(dp[n - 1])
