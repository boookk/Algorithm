"""
조합의 공식을 이용하여 m개 중에 n개를 선택하는 경우를 구하면 된다.
"""
import sys


def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


T = int(input())
for _ in range(T):
    n, m = map(int, sys.stdin.readline().split())
    print(factorial(m) // (factorial(m - n) * factorial(n)))
