import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    coin = list(map(int, input().split()))
    target = int(input())
    
    dp = [0] * (target + 1)
    
    for c in coin:
        for i in range(c, target + 1):
            if i == c:
                dp[i] += 1
            else:
                dp[i] += dp[i - c]
                
    print(dp[target])
