"""
KMP 알고리즘을 사용하고 PyPy3로 제출했다.
KMP 알고리즘은 O(n + m) 시간으로 문자열을 검색할 수 있다.
"""
string = input()

answer = 0

for idx in range(len(string)):
    pattern = string[idx:]
    length = len(pattern)
    table = [0] * length
    cnt = 0
    
    for i in range(1, length):
        while cnt > 0 and pattern[i] != pattern[cnt]:
            cnt = table[cnt - 1]
        if pattern[i] == pattern[cnt]:
            cnt += 1
            table[i] = cnt
    
    answer = max(answer, max(table))

print(answer)
