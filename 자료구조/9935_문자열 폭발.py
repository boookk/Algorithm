string = input()
delString = input()

lastChar = delString[-1]
length = len(delString)
stack = list()

for c in string:
    stack.append(c)
    if c == lastChar and ''.join(stack[-length:]) == delString:
        for _ in range(length):
            stack.pop()
    
answer = ''.join(stack)
    
print(answer if answer else 'FRULA')
