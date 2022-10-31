"""
완전 탐색으로 O(n^2)으로 해결할 수도 있겠지만, 정렬 후 다음 요소와 비교만 하면 O(n)으로 해결할 수 있다.
"""
import sys
input = sys.stdin.readline


T = int(input())
for _ in range(T):
    n = int(input())
    phoneNumbers = [input().rstrip() for _ in range(n)]
    
    phoneNumbers.sort()
    
    flag = True
    
    for i in range(n - 1):
        if phoneNumbers[i] == phoneNumbers[i + 1][:len(phoneNumbers[i])]:
            flag = False
            break
        
        if not flag:
            break
    
    print('YES' if flag else 'NO')
