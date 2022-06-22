import sys
from collections import deque


def check_left(num, direction):
    if num > 0 and gear[num][2] != gear[num + 1][6]:
        check_left(num - 1, -direction)
        gear[num].rotate(direction)


def check_right(num, direction):
    if num <= t and gear[num - 1][2] != gear[num][6]:
        check_right(num + 1, -direction)
        gear[num].rotate(direction)


input = sys.stdin.readline

t = int(input())
gear = dict()
for i in range(1, t + 1):
    gear[i] = deque(list(map(int, input().rstrip())))

k = int(input())
for _ in range(k):
    n, d = map(int, input().split())
    
    check_left(n - 1, -d)
    check_right(n + 1, -d)
    gear[n].rotate(d)

ans = 0
for i in range(1, t + 1):
    ans += gear[i][0]

print(ans)
