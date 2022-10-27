import sys
from collections import deque
input = sys.stdin.readline


def reverse(lst, start, end):
    while start <= end:
        lst[start], lst[end] = lst[end], lst[start]
        start += 1
        end -= 1
    return lst


def bfs(s):
    visited = {s: 0}
    queue = deque([s])
    answer = ''.join(sorted(permutation))
    
    while queue:
        x = queue.popleft()
        
        if x == answer:
            return visited[x]
        
        for i in range(n - k + 1):
            cp_lst = list(x[:])
            cp_x = ''.join(reverse(cp_lst, i, i + k - 1))
            
            if not visited.get(cp_x):
                visited[cp_x] = visited[x] + 1
                queue.append(cp_x)
    
    return -1


n, k = map(int, input().split())
permutation = input().rstrip().split()

print(bfs(''.join(permutation)))
