S = input()

stack = []
cnt = 0
before = 0

for c in S:
    if c == '(':
        stack.append((cnt - 1, before))
        cnt = 0
    elif c == ')':
        info = stack.pop()
        cnt = cnt * info[1] + info[0]
    else:
        cnt += 1
        before = int(c)
        
print(cnt)
