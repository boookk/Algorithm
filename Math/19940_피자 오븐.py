import sys


input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    ans = [0] * 5
    
    hour, ten, one = n // 60, (n % 60) // 10, n % 10
    
    if one > 5:
        ten += 1
        one -= 10
    if ten > 3:
        hour += 1
        ten -= 6
    if ten < 0 and one == 5:
        ten += 1
        one -= 10
    
    ans[0] = hour
    ans[2 - (ten >= 0)] = abs(ten)
    ans[4 - (one >= 0)] = abs(one)
    print(*ans)
