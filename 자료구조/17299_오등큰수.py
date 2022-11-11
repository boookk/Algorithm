n = int(input())
nums = list(map(int, input().split()))

cnt = dict()
stack = [0]
answer = [-1] * n

for num in nums:
    cnt[num] = cnt.get(num, 0) + 1

for i in range(1, n):
    while stack and cnt[nums[stack[-1]]] < cnt[nums[i]]:
        answer[stack.pop()] = nums[i]
    
    stack.append(i)

print(*answer)
