"""
사실 재귀로 피보나치 함수 구현하고 조건문에서 전역 변수로 0, 1의 개수를 셌다.
그러나 시간 초과 발생하였고 메모제이션 방법을 사용하여도 시간 초과였다.
이 문제는 fibonacci(n)을 호출한다면, 실행되는 fibonacci(0)과 fibonacci(1)은
'fibonacci(n-1)의 0과 1 호출 횟수' + 'fibonacci(n-2)의 0과 1 호출 횟수'와 동일하다는 것을 이용해서 풀어야 한다.
"""
import sys


def fibonacci(n):
    if len(zero) <= n:
        for i in range(len(zero), n+1):
            zero.append(zero[i - 1] + zero[i - 2])
            one.append(one[i - 1] + one[i - 2])
    print(zero[n], one[n])


zero = [1, 0, 1]
one = [0, 1, 1]
T = int(sys.stdin.readline())
for _ in range(T):
    fibonacci(int(sys.stdin.readline()))
