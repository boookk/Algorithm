"""
처음에는 동생들의 위치에 내 위치를 포함하여 수열의 규칙을 찾는 방법으로 풀었으나, 틀렸다.
이 문제는 내 위치와 동생들의 위치를 뺀 절댓값 간 최대공약수를 찾아 풀어야 한다.
"""

def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)


n, s = map(int, input().split())
locations = list(map(int, input().split()))

dist = list()

for loc in locations:
    dist.append(abs(loc - s))

answer = dist[0]

for i in range(1, n):
    answer = gcd(answer, dist[i])

print(answer)
