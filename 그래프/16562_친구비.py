"""
처음에는 분리 집합으로 친구 관계를 구한 후 set으로 중복된 원소를 지우고 남은 원소에 해당하는 친구비만 더했다.
그러나 [1, 1, 2, 2, 1] 이러한 친구 관계를 구하게 된다면, 한 명과 친구를 해도 모두와 친구가 될 수 있지만,
2명의 친구를 사귀어야만 모두와 친구가 될 수 있다는 결과가 나온다.
그렇기 때문에 해당 인덱스와 요소의 값이 일치할 때만 친구비를 계산해야 한다.
"""
import sys

input = sys.stdin.readline


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    a = find(a)
    b = find(b)

    if a != b:
        if friends_money[a] < friends_money[b]:
            parent[b] = a
        else:
            parent[a] = b


n, m, k = map(int, input().split())
friends_money = [0] + list(map(int, input().split()))
parent = [i for i in range(n + 1)]

for _ in range(m):
    v, w = map(int, input().split())
    union(v, w)

answer = 0
for i, v in enumerate(parent):
    if i and i == v:
        answer += friends_money[i]
print("Oh no" if answer > k else answer)
