"""
분리 집합이라는 새로운 개념을 알게 되었다..
분리 집합이란 교집합이 존재하지 않는 둘 이상의 집합을 의미한다.

보통 트리 구조를 이용한 union(), find()를 이용해 분리 집합을 구현한다.
여기서 Union은 두 분리 집합을 하나로 합치는 것, Find는 어떤 자식 노드의 최정상 부모 노드를 찾아 해당 원소가 속한 집합을 찾는 연산을 의미한다.
"""
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)


def union(x, y):
    x = find(x)
    y = find(y)

    if x > y:
        parents[x] = y
    else:
        parents[y] = x


def find(k):
    if k != parents[k]:
        parents[k] = find(parents[k])
    return parents[k]


n, m = map(int, input().split())
parents = [i for i in range(n + 1)]
for _ in range(m):
    op, a, b = map(int, input().split())
    if op:
        print("YES" if find(a) == find(b) else "NO")
    else:
        union(a, b)
