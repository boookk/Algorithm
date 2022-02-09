""" 그리디 알고리즘 (탐욕법) """

""" 첫 번째 풀이 """
n, k = map(int, input().split())
cnt = 0
while n != 1:
    if n % k: n -= 1
    else: n //= k
    cnt +=1
print(cnt)


""" 두 번째 풀이 """
n, k = map(int, input().split())
cnt = 0

while True:
    target = (n // k) * k
    cnt += (n - target)       # 1을 빼야하는 경우의 수
    n = target

    # n이 k보다 작으면 나누지 못한다.
    if n < k: break

    n //= k
    cnt += 1                  # 나누는 경우의 수

cnt += (n - 1)
print(cnt)


"""
두 번째 풀이가 첫 번째 풀이에 비해 코드의 길이가 길지만, O(logN)의 시간으로 풀이 가능하다.
"""
