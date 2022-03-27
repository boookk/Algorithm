"""
for문을 역순으로 진행하고, 1차원 dp 테이블의 값을 복사했다가 덮어쓰는 이유는 똑같은 추를 사용하지 않기 위해서다.
예를 들어 for문을 오름차순으로 진행하는 경우, 1g 추를 이용하여 dp[1] = 1 갱신하면 dp[2] = 1로 갱신하게 된다.

그리고 dp 테이블의 행을 추의 개수만큼 만들지 않고 갱신하는 형태로 코드를 작성하여 메모리 효율성을 얻었다.
i번째 추로 만들 수 있는 무게를 구할 때 i - 1번째 추를 만든 dp 테이블의 값을 이용하기 때문이다.
"""
import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
m = int(input())
marbles = list(map(int, input().split()))

dp = [0] * 40001
dp[0] = 1

for a in arr:
    tmp = dp[:]
    for j in range(sum(arr), -1, -1):
        if dp[j] == 0: continue
        if a - j >= 0: tmp[a - j] = 1
        if j - a >= 0: tmp[j - a] = 1
        tmp[a + j] = 1
    dp = tmp[:]

print(*['Y' if dp[m] else 'N' for m in marbles])
