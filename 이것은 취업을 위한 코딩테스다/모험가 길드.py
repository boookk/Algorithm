n = int(input())
rate = list(map(int, input().split()))
rate.sort()

count = 0
result = 0

for r in rate:
    count += 1
    if count >= r:
        result += 1
        count = 0
print(result)
