n, k = map(int, input().split())
result = 0
coins = [int(input()) for _ in range(n)]
coins.sort(reverse=True)

for coin in coins:
    if coin > k:
        continue
    result += k // coin
    k %= coin
print(result)
