
"""
음.. replace를 쓸 때와 인덱스 슬라이싱을 통해 문자열을 바꿔서 문자를 변경하는 것에는 차이가 있는 것 같다.
replace를 할 때 틀렸지만, 슬라이싱 했을 때는 바로 통과했다.
"""
import sys

input = sys.stdin.readline

n = int(input())
shortcut = set()
for _ in range(n):
    data = input().rstrip().split()
    for i, d in enumerate(data):
        if d[0].upper() not in shortcut:
            shortcut.add(d[0].upper())
            data[i] = '[' + d[0] + ']' + d[1:]
            
            break
    else:
        for i in range(len(data)):
            for j in range(len(data[i])):
                if data[i][j].upper() not in shortcut:
                    shortcut.add(data[i][j].upper())
                    data[i] = data[i][:j] + '[' + data[i][j] + ']' + data[i][j+1:]
                    break
            if '[' in data[i]:
                break

    print(*data)
