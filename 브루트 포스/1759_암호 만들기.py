import sys

def dfs(idx, password):
    if len(password) == l:
        cnt = 0
        for p in password:
            if p in ['a', 'e', 'i', 'o', 'u']:
                cnt += 1
        if cnt >= 1 and l - cnt >= 2:
            print(''.join(password))
        return

    if idx == c:
        return
    
    password.append(alpha[idx])
    dfs(idx + 1, password)
    password.pop()
    dfs(idx + 1, password)
    

input = sys.stdin.readline

l, c = map(int, input().split())
alpha = sorted(input().split())

dfs(0, [])
