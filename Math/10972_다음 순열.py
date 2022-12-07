n = int(input())
numbers = list(map(int, input().split()))

for i in range(n - 1, 0, -1):
    if numbers[i - 1] < numbers[i]:
        for j in range(n - 1, 0, -1):
            if numbers[i - 1] < numbers[j]:
                numbers[i - 1], numbers[j] = numbers[j], numbers[i - 1]
                numbers = numbers[:i] + sorted(numbers[i:])
                print(*numbers)
                exit(0)

print(-1)
