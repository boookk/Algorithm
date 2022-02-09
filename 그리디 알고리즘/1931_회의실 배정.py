"""
1. 회의 시간이 가장 일찍 끝나는 순서로 정렬
2. 끝나는 시간이 같을 경우, 시작 시간이 빠른 순으로 정렬
"""

n = int(input())
schedules = [tuple(map(int, input().split())) for _ in range(n)]
schedules.sort(key=lambda x: (x[1], x[0]))

count = 0
end_time = 0

for schedule in schedules:
    if end_time > schedule[0]:
        continue
    end_time = schedule[1]
    count += 1
print(count)
