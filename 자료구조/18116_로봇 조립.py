"""
분리 집합 문제인데, 11번째 줄에서 재귀 함수 find()의 값을 parents[x]에 대입하는 것을 잊어서 고생했다.
"""

import sys
input = sys.stdin.readline


def find(x):
    if parents.get(x, x) != x:
        parents[x] = find(parents[x])
    return parents.get(x, x)


def union(a, b):
    a = find(a)
    b = find(b)
    
    if a < b:
        parents[b] = a
        cnt[a] = cnt.get(a, 1) + cnt.get(b, 1)
        cnt[b] = 0
    elif b < a:
        parents[a] = b
        cnt[b] = cnt.get(a, 1) + cnt.get(b, 1)
        cnt[a] = 0


n = int(input())

parents = dict()
cnt = dict()

for _ in range(n):
    cmd = input().rstrip().split()
    
    if cmd[0] == 'I':
        union(int(cmd[1]), int(cmd[2]))
    else:
        root = find(int(cmd[1]))
        print(cnt.get(root, 1))
