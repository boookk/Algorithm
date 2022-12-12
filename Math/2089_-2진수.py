n = int(input())

if n == 0:
    print(0)
else:
    answer = ''
    
    while n != 0:
        if n % -2:
            n = n // -2 + 1
            answer = '1' + answer
        else:
            n //= -2
            answer = '0' + answer
    
    print(answer)
