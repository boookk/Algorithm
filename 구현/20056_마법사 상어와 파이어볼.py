import sys


def move_fireball(fireball):
    new_fireball = dict()
    for k, v in fireball.items():
        for m, s, d in v:
            nx = (k[0] + D[d][0] * s) % N
            ny = (k[1] + D[d][1] * s) % N
            
            if (nx, ny) not in new_fireball:
                new_fireball[(nx, ny)] = []
            new_fireball[(nx, ny)].append((m, s, d))
    
    return new_fireball


def duplication(fireball):
    new_fireball = dict()
    for k, v in fireball.items():
        if len(v) == 1:
            new_fireball[k] = [v[0]]
            continue
        
        sum_m, sum_s = 0, 0
        odd, even = False, False
        for m, s, d in v:
            sum_m += m
            sum_s += s
            if d % 2:
                odd = True
            else:
                even = True
        
        
        new_m = sum_m // 5
        if new_m == 0:
            continue
        
        new_fireball[k] = []
        new_s = sum_s // len(v)
        new_d = [0, 2, 4, 6] if odd ^ even else [1, 3, 5, 7]
        
        
        for d in new_d:
            new_fireball[k].append((new_m, new_s, d))
    
    return new_fireball


input = sys.stdin.readline

N, M, K = map(int, input().split())

fireball = dict()
for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    if (r - 1, c - 1) not in fireball:
        fireball[(r - 1, c - 1)] = []
    fireball[(r - 1, c - 1)].append((m, s, d))

D = {0: [-1, 0], 1: [-1, 1], 2: [0, 1], 3: [1, 1], 4: [1, 0], 5: [1, -1], 6: [0, -1], 7: [-1, -1]}

for _ in range(K):
    fireball = move_fireball(fireball)  # 파이어볼 이동
    fireball = duplication(fireball)    # 2개 이상의 파이어볼이 있는지 확인하여 처리

ans = 0
for k, v in fireball.items():
    for m, s, d in v:
        ans += m

print(ans)
