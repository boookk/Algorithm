"""
두 수의 합을 저장한 변수의 타입이 set이 아니라 dictionary였다면, 시간을 더 단축시킬 수 있을 것이다.
"""
import sys
input = sys.stdin.readline


n = int(input())
nums = [int(input()) for _ in range(n)]

nums.sort()

sums = set()

for i in nums:
    for j in nums:
        sums.add(i + j)

for i in range(n - 1, -1, -1):
    for j in range(i + 1):
        if nums[i] - nums[j] in sums:
            print(nums[i])
            exit(0)
