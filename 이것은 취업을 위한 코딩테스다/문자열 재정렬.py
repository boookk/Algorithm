string = input()
value = 0
result = []
for s in string:
    if s.isdigit():
        value += int(s)
    else:
        result.append(s)

result.sort()
result.append(str(value))

print(''.join(result))
