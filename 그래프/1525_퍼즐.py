import sys
from collections import deque
input = sys.stdin.readline


def bfs():
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    
    queue = deque([data])
    result[data] = 0
    
    while queue:
        puzzle = queue.popleft()
        
        if puzzle == '123456780':
            return result[puzzle]
        
        zero = puzzle.find('0')
        x, y = divmod(zero, 3)
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= 3 or ny < 0 or ny >= 3:
                continue
            
            puzzle_list = list(puzzle)
            puzzle_list[zero], puzzle_list[nx * 3 + ny] = puzzle_list[nx * 3 + ny], puzzle_list[zero]
            
            move_puzzle = ''.join(puzzle_list)
            
            if not result.get(move_puzzle):
                result[move_puzzle] = result[puzzle] + 1
                queue.append(move_puzzle)
    
    return -1


data = ''
result = dict()

for _ in range(3):
    data += input().rstrip().replace(' ', '')

print(bfs())
