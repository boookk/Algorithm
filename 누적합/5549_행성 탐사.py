import sys


input = sys.stdin.readline

n, m = map(int, input().split())
k = int(input())
maps = [input().rstrip() for _ in range(n)]

jungle = [[0] * (m + 1) for _ in range(n + 1)]
ocean = [[0] * (m + 1) for _ in range(n + 1)]
ice = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(n):
    for j in range(m):
        jungle[i + 1][j + 1] = jungle[i + 1][j] + jungle[i][j + 1] - jungle[i][j]
        ocean[i + 1][j + 1] = ocean[i + 1][j] + ocean[i][j + 1] - ocean[i][j]
        ice[i + 1][j + 1] = ice[i + 1][j] + ice[i][j + 1] - ice[i][j]
        
        if maps[i][j] == 'J':
            jungle[i + 1][j + 1] += 1
        elif maps[i][j] == 'O':
            ocean[i + 1][j + 1] += 1
        else:
            ice[i + 1][j + 1] += 1

for _ in range(k):
    a, b, c, d = map(int, input().split())
    
    j = jungle[c][d] - jungle[c][b - 1] - jungle[a - 1][d] + jungle[a - 1][b - 1]
    o = ocean[c][d] - ocean[c][b - 1] - ocean[a - 1][d] + ocean[a - 1][b - 1]
    i = ice[c][d] - ice[c][b - 1] - ice[a - 1][d] + ice[a - 1][b - 1]
    
    print(j, o, i)
