"""
원의 방정식을 이용하여 두 원의 거리를 구하면 문제를 해결할 수 있다.
"""
import math

n = int(input())

for _ in range(n):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    distance = math.sqrt((x1 - x2) ** 2 + (y1 -y2) ** 2)    # 두 원의 거리
    if distance == 0 and r1 == r2:                          # 두 원이 일치하는 경우
        print(-1)
    elif abs(r1 - r2) == distance or r1 + r2 == distance:   # 내접, 외접일 때
        print(1)
    elif abs(r1 - r2) < distance < (r1 + r2):               # 두 원이 서로 다른 두 점에서 만날 때
        print(2)
    else:                                                   # 그 외에
        print(0)  
