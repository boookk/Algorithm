"""
목록을 회전하기 위해 rotate()를 직접 구하였지만, deque.rotate()를 사용해도 좋을 것 같다
"""
import sys


def rotate(lst, d):
    if d == 1:  # 시계방향
        reverse(lst, 0, len(lst) - 2)
    else:
        reverse(lst, 1, len(lst) - 1)    
    reverse(lst, 0, len(lst) - 1)
    return lst
    

def reverse(lst, i, j):
    while i < j:
        lst[i], lst[j] = lst[j], lst[i]
        i += 1
        j -= 1


def check_right(idx, d_):
    if idx < 4 and gear[idx - 1][2] != gear[idx][6]:
        check_right(idx + 1, -d_)
        gear[idx] = rotate(gear[idx], d_)
        

def check_left(idx, d_):
    if idx >= 0 and gear[idx][2] != gear[idx + 1][6]:
        check_left(idx - 1, -d_)
        gear[idx] = rotate(gear[idx], d_)


input = sys.stdin.readline

gear = [list(map(int, input().rstrip())) for _ in range(4)]
k = int(input())

for _ in range(k):
    n, d = map(int, input().split())
    
    check_right(n, -d)
    check_left(n - 2, -d)
    gear[n - 1] = rotate(gear[n - 1], d)

ans = 0
for i in range(4):
    if gear[i][0]:
        ans += 2 ** i

print(ans)
