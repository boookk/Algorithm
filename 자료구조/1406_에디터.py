"""
태그에 연결 리스트가 있어서 처음에 연결 리스트를 구현하여 문제를 해결하려고 했으나, 시간 초과가 발생하였다.
시간을 줄이기 위해 커서를 기준으로 리스트를 양 쪽에 둔다는 생각으로 구현하고 append()와 매개변수 없이 pop()을 사용하였다.
"""
import sys


left_stack = list(input())
right_stack = []

n = len(left_stack)         # 문자열 길이

m = int(input())
for _ in range(m):
    command = sys.stdin.readline().rstrip()
    if 'L' in command:              # 왼쪽으로 커서 한 칸 이동
        if left_stack:
            item = left_stack.pop()
            right_stack.append(item)
    elif 'D' in command:            # 오른쪽으로 커서 한 칸 이동
        if right_stack:
            item = right_stack.pop()
            left_stack.append(item)
    elif 'B' in command:            # 커서 왼쪽에 있는 문자 삭제
        if left_stack:
            left_stack.pop()
    elif 'P' in command:            # 커서 왼쪽에 문자 추가
        x = command.split()[-1]
        left_stack.append(x)

print(''.join(left_stack) + ''.join(right_stack[::-1]))
