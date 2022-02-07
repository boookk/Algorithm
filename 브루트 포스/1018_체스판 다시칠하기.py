n, m = map(int, input().split())
board = []
for _ in range(n):
    board.append(input())

result = 100
for i in range(n-7):
    for j in range(m-7):
        w = 0                           # 체스판이 흰색으로 시작하는 경우
        b = 0                           # 검정색으로 시작하는 경우
        for y in range(i, i+8):
            for x in range(j, i+8):
                if (x + y) % 2 == 0:
                    if board[y][x] == 'W': b += 1
                    else: w += 1
                else:
                    if board[y][x] == 'B': b += 1
                    else: w += 1
        result = min(w, b, result)

print(result)
