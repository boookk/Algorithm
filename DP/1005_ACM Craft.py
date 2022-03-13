import sys
from collections import deque

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n, k = map(int, input().split())                    # 건물 갯수, 건물 간의 건설 순서 규칙 수
    time = [0] + list(map(int, input().split()))        # 건물이 건설되는 시간
    graph = [[] for _ in range(n + 1)]
    inDegree = [0] * (n + 1)                            # 위상 정렬을 하기 위한 진입 차수
    
    for _ in range(k):
        i, j = map(int, input().split())
        graph[i].append(j)                              # 건물 i를 지은 후 건물 j를 지을 수 있다.
        inDegree[j] += 1                                # 건물 i를 지은 후 건물 j를 지을 수 있기 때문에 j의 진입 차수를 증가시킨다.
    
    w = int(input())                                    # 승리하기 위해 지어야 하는 건물 번호

    queue = deque()
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        if inDegree[i] == 0:                            # 진입 차수가 0인 건물을 큐에 넣는다.
            queue.append(i)
            dp[i] = time[i]                             # dp 테이블에 진입 차수가 0인 건물만 건물이 건설되는 시간으로 설정해둔다.

    while queue:
        v = queue.popleft()

        for i in graph[v]:
            inDegree[i] -= 1                            # v 번째 건물 다음으로 지어질 i번째 건물의 차수를 감소시킨다.
            dp[i] = max(dp[i], time[i] + dp[v])         # i번째 건물은 v번째 건물 다음으로 지어지기 때문에 큰 값으로 변경

            if inDegree[i] == 0:                        # 건물을 계속 짓기 위해 진입 차수가 0이면 큐에 추가한다.
                queue.append(i)

    print(dp[w])
