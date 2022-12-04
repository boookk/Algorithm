import sys
input = sys.stdin.readline


T = int(input())
for _ in range(T):
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())
    
    answer = 0
    
    for _ in range(n):
        cx, cy, r = map(int, input().split())
        dist1 = ((x1 - cx) ** 2 + (y1 - cy) ** 2) ** 0.5
        dist2 = ((x2 - cx) ** 2 + (y2 - cy) ** 2) ** 0.5
        
        if r > dist1 and r > dist2:
            continue
        elif r > dist1:
            answer += 1
        elif r > dist2:
            answer += 1
    
    print(answer)
