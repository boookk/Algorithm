"""
브루트 포스 문제로 백트래킹으로 풀 수도 있지만, 조합을 사용하여 간판하게 구현하였다.
"""
from itertools import combinations


n = int(input())

lst = list()
for i in range(1, 11):
    for comb in combinations(range(10), i):
        comb = list(comb)
        comb.sort(reverse=True)
        lst.append(int(''.join(map(str, comb))))

lst.sort()
if len(lst) >= n:
    print(lst[n - 1])
else:
    print(-1)
