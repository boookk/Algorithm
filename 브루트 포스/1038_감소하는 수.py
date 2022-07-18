import sys
from itertools import combinations


input = sys.stdin.readline

n = int(input())

numbers = list()
for i in range(1, 11):
    for c in combinations(range(0, 10), i):
        c = sorted(list(c), reverse=True)
        numbers.append(int(''.join(map(str, c))))

numbers.sort()
print(numbers[n] if n < len(numbers) else -1)
