import sys
input = sys.stdin.readline


bounds = 10000

isPrime = [True for _ in range(bounds + 1)]
isPrime[0], isPrime[1] = False, False

for i in range(2, int(bounds ** 0.5 + 1)):
    if isPrime[i]:
        j = 2
        while i * j <= bounds:
            isPrime[i * j] = False
            j += 1

T = int(input())
for _ in range(T):
    n = int(input())
    
    a = b = n // 2
    while a > 0:
        if isPrime[a] and isPrime[b]:
            print(a, b)
            break
        else:
            a -= 1
            b += 1
