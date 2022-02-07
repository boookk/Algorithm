
""" 예전 풀이 """
from itertools import combinations

def solution(n, m, cards):
    answer = 0
    for combo in list(combinations(cards, 3)):
        if sum(combo) > m:
            continue
        answer = max(answer, sum(combo))
    return answer
    
    
n, m = map(int, input().split())
cards = list(map(int, input().split()))
print(solution(n, m, cards))


""" 현재 풀이 """
n, m = map(int, input().split())
cards = list(map(int, input().split()))
result = 0

for i in range(len(cards)):
    for j in range(len(cards)):
        for k in range(len(cards)):
            if i == j or j == k or k == i: continue
            total = cards[i] + cards[j] + cards[k]
            if total > m: continue
            result = max(total, result)

print(result)



"""
예전에 풀었을 때, combinations 라이브러리를 사용하여 3개의 카드를 찾는 경우 모든 경우를 찾아서 m보다 크지 않으면서 가장 큰 값을 찾았다.
현재는 Unpacking operation을 통해 출력하였다.
그 결과 실행 시간이 증가했다.

라이브러리를 사용하지 않으면 수행 시간이 감소할 줄 알았지만 삼중 for문은 O(n^3)의 시간 복잡도를 가진다.
두 풀이의 시간은 약 4배정도 차이난다.
"""
