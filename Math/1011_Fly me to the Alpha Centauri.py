T = int(input())
for _ in range(T):
    x, y = map(int, input().split())
    
    dist = y - x
    cnt = 0
    
    while True:
        if dist <= cnt * (cnt + 1):
            break
        cnt += 1
    
    if dist <= cnt ** 2:
        cnt = cnt * 2 - 1
    else:
        cnt = cnt * 2
    
    print(cnt)
