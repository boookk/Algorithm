n, k = map(int, input().split())
num = list(input())

stack = list()

for i in range(n):
    while stack and stack[-1] < num[i] and k > 0:
        stack.pop()
        k -= 1
    stack.append(num[i])

print(''.join(stack[:-k]) if k > 0 else ''.join(stack))
