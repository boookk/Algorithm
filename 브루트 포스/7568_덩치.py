""" 예전 풀이 """
n = int(input())

people = []
for i in range(n):
    people.append(list(map(int, input().split())))

rank = [1] * n
for i in range(n):
    for j in range(n):
        if people[i][0] < people[j][0] and people[i][1] < people[j][1]:
            rank[i] += 1
    
print(' '.join(map(str, rank)))


""" 현재 풀이 """
n = int(input())
rank = [1] * n
people = []
for _ in range(n):
    people.append(list(map(int, input().split())))
for i, (w, h) in enumerate(people):
    for person in people:
        if w < person[0] and h < person[1]:
            rank[i] += 1
print(*rank)


"""
예전에 풀었을 때, 결과를 정수였던 리스트 요소를 문자열로 바꾸고 join 함수를 사용하여 출력하였다.
현재는 Unpacking operation을 통해 출력하였다.

그 결과 실행시간 약간 단축되었다.
"""
