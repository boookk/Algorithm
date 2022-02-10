""" 첫 시도 (57점) """
n = int(input())
distance = list(map(int, input().split()))
price = list(map(int, input().split()))

result = 0
end = n

for p in sorted(price[:-1]):
    tmp = price.index(p)
    if tmp > end:
        continue
    result += p * sum(distance[tmp:end])
    end = tmp

print(result)


""" 두 번째 시도 (100점) """
n = int(input())
distance = list(map(int, input().split()))
price = list(map(int, input().split()))

result = 0
min_price = price[0]
for i in range(n-1):
    if min_price > price[i]:
        min_price = price[i]
    result += min_price * distance[i]
print(result)



"""
처음 시도할 때 마지막 도시를 제외한 도시들의 가격을 정렬하여 계산했더니, 57점을 받았다.
그래서 정말 그리디한 알고리즘으로 해결하였다.
복잡하게 생각한 것이 부분 점수를 받은 요인인 것 같다.
"""
