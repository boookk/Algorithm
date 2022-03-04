"""
가장 긴 증가하는 부분 수열로 해결하면 된다고 한다 !
"""
n = int(input())
arr = list(map(int, input().split()))
arr.reverse()

dp = [1] * n

for i in range(1, n):
    for j in range(0, i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j] + 1)
print(n - max(dp))
