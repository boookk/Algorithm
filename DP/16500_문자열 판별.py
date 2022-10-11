import sys
input = sys.stdin.readline


def func(idx):
    global answer
    
    if idx == len(s):
        answer = 1
        return
    
    if dp[idx]:
        return
    
    dp[idx] = 1
    
    for i in range(n):
        if len(s[idx:]) >= len(word_list[i]):
            for j in range(len(word_list[i])):
                if s[idx+j] != word_list[i][j]:
                    break
            else:
                func(idx + len(word_list[i]))


s = input().rstrip()
n = int(input())
word_list = [input().rstrip() for _ in range(n)]

dp = [0] * 101
dp[len(s)] = 1

answer = 0
func(0)
print(answer)
