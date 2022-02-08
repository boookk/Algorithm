""" 예전 풀이 """
n = int(input())

number = []
for i in range(n):
    number.append(int(input()))

number.sort()
for num in number:
    print(num)


""" 버블 정렬 """
n = int(input())
numbers = []
for _ in range(n):
    numbers.append(int(input()))

for i in range(len(numbers)):
    for j in range(0, len(numbers)-i-1):
        if numbers[j] > numbers[j+1]:
            numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

print(*numbers, sep='\n')



""" 삽입 정렬 """
n = int(input())
numbers = []
for _ in range(n):
    numbers.append(int(input()))

for i in range(1, n):
    tmp = numbers[i]
    idx = i - 1
    while tmp < numbers[idx] and idx > -1:
        numbers[idx+1] = numbers[idx]
        idx -= 1
    numbers[idx+1] = tmp

print(*numbers, sep='\n')



"""
예전에 풀었을 때는 라이브러리를 사용하여 빠르게 풀었다.
현재는 라이브러리를 사용하지 않고 버블 정렬 알고리즘과 삽입 정렬 알고리즘을 구현하여 문제를 해결하였다.
"""
