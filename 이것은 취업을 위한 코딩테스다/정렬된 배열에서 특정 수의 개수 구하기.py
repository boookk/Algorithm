from bisect import bisect_right, bisect_left

n, x = map(int, input().split())
arr = list(map(int, input().split()))

count = bisect_right(arr, x) - bisect_left(arr, x)

if count:
    print(count)
else:
    print(-1)
