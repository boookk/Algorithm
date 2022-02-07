n = int(input())

k = 666
cnt = 0
while True:
    if '666' in str(k): cnt += 1
    if n == cnt: break
    k += 1

print(k)
