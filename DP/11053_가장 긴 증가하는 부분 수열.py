"""
최장 증가 부분 수열 문제를 이분탐색에서 풀었기 때문에 첫 번째 풀이와 같이 제출했다.
그런데 알고리즘 분류를 보니 다이나믹 프로그래밍이었기 때문에 두 번째 풀이와 같이 구현하였다.
"""


""" 첫 번째 풀이 """
import bisect

n = int(input())
arr = list(map(int, input().split()))
dp = []
for a in arr:
    index = bisect.bisect_left(dp, a)
    if len(dp) <= index:
        dp.append(a)
    else:
        dp[index] = a
print(len(dp))


""" 두 번째 풀이 """
n = int(input())
arr = list(map(int, input().split()))
dp = [1] * n
for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)
print(max(dp))
