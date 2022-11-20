expression = input()

stack = list()
answer = ''

for exp in expression:
    if exp.isalpha():
        answer += exp
    else:
        if exp == '(':
            stack.append(exp)
        elif exp in ['*', '/']:
            while stack and (stack[-1] in ['*', '/']):
                answer += stack.pop()
            stack.append(exp)
        else:
            while stack and stack[-1] != '(':
                answer += stack.pop()
            if exp == ')':
                stack.pop()
            else:
                stack.append(exp)

while stack:
    answer += stack.pop()

print(answer)
