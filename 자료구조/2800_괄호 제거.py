"""
본 문제는 자료구조, 스택, 재귀 문제다.
재귀로 문제를 풀게 되면 자연스럽게 스택을 사용한다.
다른 풀이를 보면 대부분 combinations 라이브러리를 사용하여 문제를 해결한다.
재귀대신 combinations 라이브러리를 사용하면 시간을 단축할 수 있지만, 라이브러리 의존도를 낮추기 위해 재귀로 해결했다.
"""
def f(idx, string):
    if idx == len(expression):
        answer.add(''.join(string))
        return
    
    if expression[idx] == '(':
        visited[idx] = True
        f(idx + 1, string)
        visited[idx] = False
    
    if expression[idx] == ')' and visited[pair[idx]]:
        visited[idx] = True
        f(idx + 1, string)
        visited[idx] = False
    else:
        string.append(expression[idx])
        f(idx + 1, string)
        string.pop()
        

expression = input()

answer = set()
stack = list()
pair = dict()
visited = [False] * len(expression)

for i, c in enumerate(expression):
    if c == '(':
        stack.append(i)
    elif c == ')':
        pair[i] = stack.pop()

f(0, [])
answer.remove(expression)
print(*sorted(list(answer)), sep='\n')
