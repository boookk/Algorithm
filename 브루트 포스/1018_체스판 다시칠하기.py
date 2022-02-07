n, m = map(int, input().split())
board = []
for _ in range(n):
    board.append(input())

result = 100
for i in range(n-7):
    for j in range(m-7):
        w = 0
        b = 0
        for y in range(i, i+8):
            for x in range(j, i+8):
                if (x + y) % 2 == 0:
                    if board[y][x] == 'W': b += 1 # 짝수 칸이 검정이어야 하는데, 흰색인 경우
                    else: w += 1 # 짝수 칸이 흰색이어야 하는데 검정색인 경우
                else:
                    if board[y][x] == 'B': b += 1 # 홀수 칸이 흰색이어야 하는데 검정인 경우
                    else: w += 1 # 홀수 칸이 검정이어야 하는데 검정인경우
        result = min(w, b, result)

print(result)
