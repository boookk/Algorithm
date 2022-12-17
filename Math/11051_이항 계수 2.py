"""
조합 공식 변형을 활용하여 시간 복잡도를 줄였다.
"""
n, k = map(int, input().split())

result = 1
for i in range(k):
    result *= n
    n -= 1

tmp = 1
for i in range(2, k + 1):
    tmp *= i

print((result // tmp) % 10007)
