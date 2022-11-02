import sys
from collections import deque
sys.stdin = open("data.txt", 'r')
input = sys.stdin.readline


n, k = map(int, input().split())

answer = 0
length_lst = list()
length_cnt = dict()

for i in range(n):
    length = len(input().rstrip())
    if not length in length_cnt:
        length_cnt[length] = 0
    if i > k:
        length_cnt[length_lst[i - k - 1]] -= 1
    
    answer += length_cnt[length]
    length_cnt[length] += 1
    length_lst.append(length)

print(answer)
