"""
에라토스테네스의 체로 풀게 되어도 시간 초과가 발생한다.
문제를 해결하기 위해 미리 소수 판별해야 한다.
"""
import sys
input = sys.stdin.readline


bounds = 123456

isPrime = [True for _ in range(2 * bounds + 1)]
isPrime[0], isPrime[1] = False, False

for i in range(2, int((2 * bounds) ** 0.5 + 1)):
    if isPrime[i]:
        j = 2
        while i * j <= 2 * bounds:
            isPrime[i * j] = False
            j += 1

while True:
    n = int(input())
    
    if  n == 0:
        break
    
    answer = 0
    
    for i in range(n + 1, 2 * n + 1):
        if isPrime[i]:
            answer += 1
    
    print(answer)
