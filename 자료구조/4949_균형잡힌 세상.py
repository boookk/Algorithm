import sys


while True:
    command = sys.stdin.readline().rstrip()
    if command == '.':
        break

    stack = []
    for c in command:
        if c == '(':
            stack.append('(')
            continue
        elif c == '[':
            stack.append('[')
            continue
        elif c == ')':
            if not stack or stack[-1] != '(':
                stack.append(')')
                break
            stack.pop()
        elif c == ']':
            if not stack or stack[-1] != '[':
                stack.append(']')
                break
            stack.pop()

    if len(stack) > 0:
        print('no')
    else:
        print('yes')
