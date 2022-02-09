"""
대기 시간이 작은 순서로 정렬한 후 계산하면, 각 사람이 돈을 인출하는 데 필요한 시간의 최소값을 구할 수 있다.
"""

n = int(input())
waiting_time = list(map(int, input().split()))
waiting_time.sort()

result = 0
for i in range(n):
    result += sum(waiting_time[:i+1])
print(result)
