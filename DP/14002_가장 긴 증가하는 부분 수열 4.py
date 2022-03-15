"""
가장 긴 증가하는 부분 수열을 출력하는 부분에서 굉장히 많이 틀렸다.
우선, 원래의 dp 테이블에 숫자를 바로 넣는 방식이었는데, 이는 기존의 수열을 순서를 어기는 바람에 dp 테이블에 순서를 담게 되었다.
출력할 때는 출력할 리스트와 크기를 정해준 후, dp 테이블을 순서대로 탐색하며 출력할 리스트의 값을 갱신하는 방법으로 하였다.
그러나 계속 틀렸고, dp 테이블을 뒤에서부터 탐색하며 max_size 변수를 이용하여 가장 긴 증가하는 부분 수열을 출력할 수 있었다.
"""

import sys

input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().split()))
dp = [1] * n

for i in range(n):
    for j in range(i):
        if numbers[i] > numbers[j]:
            dp[i] = max(dp[i], dp[j] + 1)

max_size = max(dp)
print(max_size)

lis = []
for i in range(n-1, -1, -1):
    if dp[i] == max_size:
        lis.append(numbers[i])
        max_size -= 1

print(*lis[::-1], sep=' ')
