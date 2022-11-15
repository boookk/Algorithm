import sys
input = sys.stdin.readline


def func(command, num):
    stack = [num]
    
    for cmd in commands:
        if cmd[:3] == 'NUM':
            stack.append(int(cmd[4:]))
        elif not stack:
            return 'ERROR'
        elif cmd == 'POP':
            stack.pop()
        elif cmd == 'INV':
            stack[-1] *= -1
        elif cmd == 'DUP':
            stack.append(stack[-1])
        elif len(stack) == 1:
            return 'ERROR'
        elif cmd == 'SWP':
            stack[-1], stack[-2] = stack[-2], stack[-1]
        elif cmd == 'ADD':
            stack.append(stack.pop() + stack.pop())
        elif cmd == 'SUB':
            stack.append(-stack.pop() + stack.pop())
        elif cmd == 'MUL':
            stack.append(stack.pop() * stack.pop())
        elif cmd == 'DIV':
            a, b = stack.pop(), stack.pop()
            if not a:
                return 'ERROR'
            tmp = abs(b) // abs(a)
            if (a > 0 and b < 0) or (a < 0 and b > 0):
                tmp *= -1
            stack.append(tmp)
        elif cmd == 'MOD':
            a, b = stack.pop(), stack.pop()
            if not a:
                return 'ERROR'
            tmp = abs(b) % abs(a)
            if b < 0:
                tmp *= -1
            stack.append(tmp)
        else:
            return 'ERROR'

        if stack and abs(stack[-1]) > 10 ** 9:
            return 'ERROR'
    
    return stack[0] if len(stack) == 1 else 'ERROR'


while True:
    commands = list()
    
    while True:
        cmd = input().strip()
        
        if cmd == 'QUIT':
            quit()
        if cmd == 'END':
            break
        
        commands.append(cmd)
    
    n = int(input())
    
    
    for _ in range(n):
        print(func(commands, int(input())))
    
    print()
    input()
