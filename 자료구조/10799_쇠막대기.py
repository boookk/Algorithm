sticks = input()
stack = []
result = 0

for i, stick in enumerate(sticks):
    if stick == '(':
        stack.append('(')
        continue

    stack.pop()

    if sticks[i - 1] == '(':        # 이전에 '(' 였다면, 레이저 지점
        result += len(stack)
    else:
        result += 1                 # 막대기 남은 끝부분 더하기

print(result)
