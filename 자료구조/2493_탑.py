n = int(input())
towers = list(map(int, input().split()))

stack = list()
answer = [0] * n

for i in range(n):
    while stack and stack[-1][1] < towers[i]:
        stack.pop()
        
    if stack:
        answer[i] = stack[-1][0]

    stack.append((i + 1, towers[i]))

print(*answer)
