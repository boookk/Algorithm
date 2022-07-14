"""
이 문제를 해결하면서 2가지 어려운 점이 있었다.
첫 번째로는 배열의 요소가 0개일 경우, 16행에서 ['']와 같이 처리된다는 점이다.
위의 경우에서 함수 D를 수행한다면 error를 발생시켜야 하지만, ''가 요소로 남아있기 때문에 원하는 결과를 얻을 수 없었다.
이를 21행에서 if문으로 처리해주었다.
다음으로 함수 D가 수행될 때 배열이 비어있을 경우에만 에러를 출력한다는 점이다.
이를 간과하여 무조건 배열이 비어있다면 error를 출력하도록 했었다.
"""

import sys
from collections import deque


input = sys.stdin.readline

T = int(input())

for _ in range(T):
    p = input().rstrip()
    n = int(input())
    queue = deque(input().rstrip()[1:-1].split(','))
    r = 0
    
    if n == 0:
        queue = deque()
    try:
        for p_ in p:
            if p_ == 'D':
                if r % 2:
                    queue.pop()
                else:
                    queue.popleft()
            else:
                r += 1
        
        if r % 2:
            queue.reverse()
        
        answer = ','.join(queue)
        print(f'[{answer}]')
    except:
        print('error', end='\n')
