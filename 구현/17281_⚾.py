"""
PyPy3로 제출
해당 문제는 굉장히 타이트한 시간 제한이 있었다.
이를 극복하고자 리스트, 변수 사용을 최대한 줄였다.
주자를 b1, b2, b3 대신 리스트로 사용하게 되면 시간 초과가 발생한다.
또한, cur_inning[line_up[idx]] 부분을 미리 변수에 할당하여 if문을 돌리면 시간 초과가 발생한다.
깔끔해 보일 수 있는 코드이지만, 시간적으로 효율적이지 못하다는 것을 알았다.
"""
import sys
from itertools import permutations


def dfs(line_up):
    score = 0
    idx = 0
    
    for cur_inning in inning:
        out = 0
        b1, b2, b3 = 0, 0, 0
        while out < 3:
            if cur_inning[line_up[idx]] == 0:
                out += 1
            elif cur_inning[line_up[idx]] == 1:
                score += b3
                b1, b2, b3 = 1, b1, b2
            elif cur_inning[line_up[idx]] == 2:
                score += (b2 + b3)
                b1, b2, b3 = 0, 1, b1
            elif cur_inning[line_up[idx]] == 3:
                score += (b1 + b2 + b3)
                b1, b2, b3 = 0, 0, 1
            elif cur_inning[line_up[idx]] == 4:
                score += (1 + b1 + b2 + b3)
                b1, b2, b3 = 0, 0, 0
            
            idx = (idx + 1) % 9
    
    return score


input = sys.stdin.readline

n = int(input())
inning = [list(map(int, input().split())) for _ in range(n)]

ans = 0

for line_up in permutations(range(1, 9), 8):
    line_up = list(line_up[:3]) + [0] + list(line_up[3:])   # e.g. [2번 선수, 5번 선수, ...]
    ans = max(ans, dfs(line_up))

print(ans)
