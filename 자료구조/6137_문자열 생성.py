import sys
input = sys.stdin.readline


n = int(input())
s = [input().rstrip() for _ in range(n)]

answer = ''
left, right = 0, n - 1
cnt = 0

while left <= right:
    if s[left] < s[right]:
        answer += s[left]
        left += 1
    elif s[left] > s[right]:
        answer += s[right]
        right -= 1
    else:
        # print(answer)
        left_, right_ = left + 1, right - 1
        while left_ <= right_:
            if s[left_] == s[right_]:
                left_ += 1
                right_ -= 1
                continue
            
            if s[left_] < s[right_]:
                answer += s[left]
                left += 1
            else:
                answer += s[right]
                right -= 1
            break
        else:
            answer += s[left]
            left += 1
    
    cnt += 1
    if cnt % 80 == 0:
        answer += '\n'

print(answer)
