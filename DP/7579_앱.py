"""
배낭 문제 응용이다.
비활성화 했을 때 비용들의 합만큼 dp 테이블을 만들고, 각 요소에는 비활성화했을 때 생기는 메모리의 용량을 담는다.
"""
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
active = [0] + list(map(int, input().split()))
memory = [0] + list(map(int, input().split()))
dp = [[0] * (sum(memory) + 1) for _ in range(n + 1)]

result = float('inf')
for i in range(1, n + 1):
    for j in range(sum(memory) + 1):
        if j >= memory[i]:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - memory[i]] + active[i])
        else:
            dp[i][j] = dp[i - 1][j]
            
        if dp[i][j] >= m:
            result = min(result, j)
            break

print(result)
