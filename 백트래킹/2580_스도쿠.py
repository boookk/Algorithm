from itertools import chain


def dfs(idx):
    if idx == len(zeros):
        for row in graph:
            print(*row)
        exit(0)

    x, y = zeros[idx]
    sub = set(chain(*[graph[i][y // 3 * 3: y // 3 * 3 + 3] for i in range(x // 3 * 3, x // 3 * 3 + 3)]))
    possibles = set(range(1, 10)) - sub - set(graph[x]) - set([graph[i][y]for i in range(9)])
    for num in possibles:
        graph[x][y] = num
        dfs(idx + 1)
        graph[x][y] = 0


graph = [list(map(int, input().split())) for _ in range(9)]
zeros = [(i, j) for i in range(9) for j in range(9) if graph[i][j] == 0]

dfs(0)
