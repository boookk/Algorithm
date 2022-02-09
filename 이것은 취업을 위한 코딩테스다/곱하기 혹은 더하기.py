""" 그리디 알고리즘 (탐욕법) """

""" 첫 번째 풀이 """
numbers = list(map(int, input()))
numbers.sort()
result = numbers[0]
for i in range(1, len(numbers)):
    if result == 0: result += numbers[i]
    else: result *= numbers[i]
print(result)


""" 두 번째 풀이 """
numbers = list(map(int, input()))
result = numbers[0]
for i in range(1, len(numbers)):
    if numbers[i] <= 1 or result <= 1: result += numbers[i]
    else: result *= numbers[i]
print(result)


"""
두 코드의 차이는 sort() 사용 여부이다.
sort()의 경우 O(NlogN)의 시간 복잡도를 가지기 때문에 입력이 많을 경우, 두 번째 풀이보다 전체 실행 시간이 증가할 것이다.

그리고 첫 번째 풀이의 경우 입력이 1일 때를 고려하지 못했다.
1일 경우 곱하는 것보다 더하는 것이 더 큰수를 만들 수 있다.
"""
