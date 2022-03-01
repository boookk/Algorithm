import sys


T = int(input())
for _ in range(T):
    stack = []
    flag = False
    string = sys.stdin.readline().rstrip()
    for s in string:
        if s == '(':
            stack.append(1)
        else:
            if not stack:
                flag = True
                break
            stack.pop()
    if stack or flag:
        print('NO')
    else:
        print('YES')
