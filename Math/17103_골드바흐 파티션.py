import sys
input = sys.stdin.readline


T = int(input())
numbers = [int(input()) for _ in range(T)]

maxNum = max(numbers)
isPrime = [True for _ in range(maxNum + 1)]
isPrime[0], isPrime[1] = False, False

for i in range(2, int(maxNum ** 0.5) + 1):
    if isPrime[i]:
        j = 2
        while i * j < maxNum:
            isPrime[i * j] = False
            j += 1

for num in numbers:
    answer = 0
    for i in range(2, num // 2 + 1):
        if isPrime[i] and isPrime[num - i]:
            answer += 1
    print(answer)
