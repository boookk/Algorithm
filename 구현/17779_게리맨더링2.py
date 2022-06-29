import sys


def get_diff(x, y, d1, d2):
    ward = [0] * 5
    
    c = y + 1
    for r in range(x + d1): # 1
        if r >= x:
            c -= 1
        ward[0] += sum(population[r][:c])
    
    c = y + 1
    for r in range(x + d2 + 1): # 2
        if r > x:
            c += 1
        ward[1] += sum(population[r][c:])
    
    c = y - d1
    for r in range(x + d1, n):  # 3
        ward[2] += sum(population[r][:c])
        if r < x + d1 + d2:
            c += 1
    
    c = y + d2
    for r in range(x + d2 + 1, n):  # 4
        ward[3] += sum(population[r][c:])
        if r <= x + d1 + d2:
            c -= 1
    
    ward[4] = total - sum(ward[:4]) # 5
    return max(ward) - min(ward)


input = sys.stdin.readline

n = int(input())

population = []
total = 0
for _ in range(n):
    population.append(list(map(int, input().split())))
    total += sum(population[-1])

ans = float('inf')
for i in range(n - 2):
    for j in range(n - 1):
        for d1 in range(1, n - 1):
            for d2 in range(1, n - 1):
                if 0 <= i + d1 + d2 < n and 0 <= j - d1 < j + d2 < n:
                    ans = min(ans, get_diff(i, j, d1, d2))

print(ans)
