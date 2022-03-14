"""
아래와 같이 두 가지를 고려해야 한다.
1. 시작점과 끝점이 같을 때 (ex. 시작점 : 2, 끝나는 점 : 2)
2. 비교해야 하는 길이가 2일 때 (ex. 1부터 3까지 팰린드롬을 이루는지 ?)
그 외에는 양 끝 문자를 비교하고 start + 1, end - 1번째 문자를 비교한다.
이를 dp 테이블을 이용하여 수행 시간을 줄인다.
"""

import sys
input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().split()))

dp = [[0] * n for _ in range(n)]

for i in range(n):
    for start in range(n - i):
        end = i + start
        if start == end:
            dp[start][end] = 1
        elif numbers[start] == numbers[end]:
            if start + 1 == end or dp[start + 1][end - 1]: dp[start][end] = 1


m = int(input())
for _ in range(m):
    s, e = map(int, input().split())
    print(dp[s - 1][e - 1])
