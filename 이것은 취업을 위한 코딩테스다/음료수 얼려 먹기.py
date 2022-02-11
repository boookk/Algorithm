def dfs(x, y):
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    # 주어진 범위 확인
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False

    if board[x][y] == 0:
        board[x][y] = 1
        # 연결된 모든 곳을 방문 처리 하기 위한 재귀적으로 호출
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny)
        return True

    return False


n, m = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int, input())))

count = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j):
            count += 1

print(count)
