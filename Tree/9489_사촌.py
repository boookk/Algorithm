import sys
input = sys.stdin.readline

while True:
    n, k = map(int, input().split())
    
    if n == k == 0:
        break
    
    nodes = list(map(int, input().split()))
    
    parents = {0: 0, nodes[0]: 0}
    idx = 0
    answer = 0
    
    for i in range(1, n):
        parents[nodes[i]] = nodes[idx]
        if i < n - 1 and nodes[i] + 1 < nodes[i + 1]:
            idx += 1
    
    if parents[parents[k]]:
        for node in nodes:
            if parents[parents[k]] == parents[parents[node]] and parents[k] != parents[node]:
                answer += 1
    
    print(answer)
