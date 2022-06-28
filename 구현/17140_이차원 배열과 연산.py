import sys


def operation(arr):
    m_col = 0
    for i in range(len(arr)):
        count = dict()
        for a in arr[i]:    # 빈도 카운팅
            if a == 0:
                continue
            if a not in count:
                count[a] = 0
            count[a] += 1
        
        tmp = sorted(count.items(), key= lambda x: (x[1], x[0]))
        
        if len(tmp) > 50:
            tmp = tmp[:50]
        
        arr[i] = []
        for t in tmp:   # [(), (), ... ()] -> [ ]
            arr[i] += t
            
        m_col = max(m_col, len(arr[i]))
    
    for i in range(len(arr)):   # 각 행 길이 맞추기
        if len(arr[i]) < m_col:
            arr[i] += [0] * (m_col - len(arr[i]))


input = sys.stdin.readline

r, c, k = map(int, input().split())
r, c = r - 1, c - 1

graph = [list(map(int, input().split())) for _ in range(3)]

ans = 0
while True:
    if len(graph) > r and len(graph[0]) > c:
        if graph[r][c] == k:
            break
    
    if len(graph) >= len(graph[0]):
        operation(graph)
    else:
        graph = list(map(list, zip(*graph)))
        operation(graph)
        graph = list(map(list, zip(*graph)))
    
    ans += 1

    if ans > 100:
        ans = -1
        break

print(ans)
