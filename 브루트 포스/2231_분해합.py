
""" 예전 풀이 """
def solution(n):
    for i in range(1, n + 1):
        tmp = i + sum(list(map(int, str(i))))
        if tmp == n:
            return i
    return 0

n = int(input())
print(solution(n))


""" 현재 풀이 """
n = int(input())

for num in range(n):
    total = num + sum(list(map(int, str(num))))
    if total == n:
        print(num)
        break
else:
    print(0)


"""
예전에 풀었을 때는 프로그래머스 문제를 풀다가 넘어온지 별로 안 돼서 함수로 구현하였다.
현재는 함수로 구현하지 않았다.
"""
