m, n = map(int, input().split())

answer = list()

for num in range(m, n + 1):
    if num < 2:
        continue
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            break
    else:
        answer.append(num)

print(*answer, sep='\n')
