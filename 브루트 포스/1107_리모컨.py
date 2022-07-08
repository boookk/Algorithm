import sys

input = sys.stdin.readline

n = int(input())
m = int(input())
lst = list(map(int, input().split()))

ans = abs(n - 100)

for i in range(1000001):
    for j in str(i):
        if int(j) in lst:
            break
    else:
        ans = min(ans, len(str(i)) + abs(i - n))

print(ans)
