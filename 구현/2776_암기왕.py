'''
두 개의 수첩을 모두 list로 만들면 시간 초과 발생
수첩1은 set으로 만들고 출력되는 순서를 유지하기 위해 수첩2는 리스트로 만든다.
'''
import sys

input = sys.stdin.readline


T = int(input())
for _ in range(T):
    n = int(input())
    lst1 = set(map(int, input().split()))
    m = int(input())
    lst2 = list(map(int, input().split()))
    
    for i in lst2:
        print(1 if i in lst1 else 0)
