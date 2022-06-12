'''
그동안 풀었던 문제와 다르게 신선했다.
DP 문제라고 하면 점화식을 찾아야 하지만, 이 문제는 인접한 부분의 합을 구한다.
'''
import sys           
                
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    dp = [1 for _ in range(10)]
    
    for _ in range(1, n):
        d = dp[:]
        dp[0] = d[7]
        dp[1] = d[2] + d[4]
        dp[2] = d[1] + d[3] + d[5]
        dp[3] = d[2] + d[6]
        dp[4] = d[1] + d[5] + d[7]
        dp[5] = d[2] + d[4] + d[6] + d[8]
        dp[6] = d[3] + d[5] + d[9]
        dp[7] = d[4] + d[8] + d[0]
        dp[8] = d[5] + d[7] + d[9]
        dp[9] = d[6] + d[8]
        
    print(sum(dp) % 1234567)
