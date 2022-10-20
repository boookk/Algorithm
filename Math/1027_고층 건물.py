n = int(input())
buildings = list(map(int, input().split()))

answer = 0

for x1, y in enumerate(buildings):
    
    cnt_right = 0
    max_right = -float('inf')
    for x2 in range(x1 + 1, n):
        right = (buildings[x2] - y) / ((x2 + 1) - (x1 + 1))
        if max_right < right:
            max_right = right
            cnt_right += 1
    
    cnt_left = 0
    max_left = float('inf')
    for x2 in range(x1 - 1, -1, -1):
        left = (buildings[x2] - y) / ((x2 + 1) - (x1 + 1))
        if max_left > left:
            max_left = left
            cnt_left += 1

    answer = max(answer, (cnt_left + cnt_right))

print(answer)
