import sys


def dfs(a, b, cnt):
    if a > b:
        return -1

    if a == b:
        return cnt

    c1 = dfs(a * 2, b, cnt + 1)
    c2 = dfs(int(str(a) + '1'), b, cnt + 1)

    if c2 < 0 < c1:
        return c1
    if c1 < 0 < c2:
        return c2

    return min(c1, c2)


input = sys.stdin.readline

a, b = map(int, input().split())

print(dfs(a, b, 1))
