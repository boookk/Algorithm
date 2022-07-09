"""
1. 경계 조건을 설정하기 위해 인수분해를 진행한다.
  - A ** 2 - B ** 2 = (A - B)(A + B)
2. 위의 식에 따라 2가지 조건을 얻을 수 있다.
  - A > B
  - A - B >= 1
  - A + B <= G
3. 두 포인터 알고리즘으로 해결
  - 시작점과 끝점이 있는데, 초기에 두 개의 점이 최소값을 가르킨다.
  - 여기서는 몸무게가 가장 적게 차이날 때가 1이기 때문에 두 포인터를 1로 세팅했다.
"""
G = int(input())
ans= []
start, end = 1, 1

while start + end <= G:
    diff = start ** 2 - end ** 2
    
    if diff == G:
        ans.append(start)
        start += 1
    elif diff < G:
        start += 1
    else:
        end += 1

if ans:
    print(*ans, sep='\n')
else:
    print(-1)
