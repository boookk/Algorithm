"""
이분 탐색 라이브러리를 사용하는 편이 빠르다 😊
"""


""" 이분 탐색 구현 """
n = int(input())
n_arr = list(map(int, input().split()))
m = int(input())
m_arr = list(map(int, input().split()))

result = [0] * m
n_arr.sort()
for i in range(m):
    start = 0
    end = n - 1
    while start <= end:
        mid = (start + end) // 2
        if n_arr[mid] == m_arr[i]:
            result[i] = 1
            break
        else:
            if n_arr[mid] < m_arr[i]:
                start = mid + 1
            else:
                end = mid - 1

print(*result, sep='\n')



""" 이분 탐색 라이브러리 사용 """
from bisect import bisect_left

n = int(input())
n_arr = list(map(int, input().split()))
n_arr.sort()

m = int(input())
m_arr = list(map(int, input().split()))

result = [0] * m
for i in range(m):
    idx = bisect_left(n_arr, m_arr[i])
    if idx >= n:
        continue
    if n_arr[idx] == m_arr[i]:
        result[i] = 1
print(*result, sep='\n')
