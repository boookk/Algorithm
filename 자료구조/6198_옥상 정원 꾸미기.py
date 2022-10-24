import sys
input = sys.stdin.readline


n = int(input())
buildings = [int(input()) for _ in range(n)]

answer = 0
stack = [buildings[0]]

for i in range(n):
    while stack and stack[-1] <= buildings[i]:
        stack.pop()
    
    stack.append(buildings[i])
    answer += len(stack) - 1

print(answer)
