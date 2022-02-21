"""
증가하는 수열 중에 가장 긴 수열을 찾는 것 같은데 다른 사람들의 풀이가 이해되지 않아서 찾아봤다.
최장 증가 부분 수열 (LIS : Longest Increasing Subsequence)을 찾는 문제라고 한다..
정리해서 포스팅해야겠다. 😂
"""
from bisect import bisect_left

n = int(input())
arr = list(map(int, input().split()))
lis = []

for a in arr:
    idx = bisect_left(lis, a)
    if len(lis) <= idx:
        lis.append(a)
    else:
        lis[idx] = a

print(len(lis))
