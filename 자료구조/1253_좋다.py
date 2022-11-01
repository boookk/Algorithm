"""
완전 탐색 대신 투 포인터 알고리즘을 사용하게 되면 O(n)으로 해결할 수 있다.
투 포인터 알고리즘은 이진탐색과 비슷한 느낌이었다.
"""

n = int(input())
lst = list(map(int, input().split()))

lst.sort()

answer = 0

for i in range(n):
    tmp = lst[:i] + lst[i + 1:]
    start, end = 0, len(tmp) - 1

    while start < end:
        num = tmp[start] + tmp[end]
        
        if num == lst[i]:
            answer += 1
            break
        
        if num < lst[i]:
            start += 1
        else:
            end -= 1

print(answer)
