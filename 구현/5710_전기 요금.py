import sys


def get_wh(cost):
    costs = [100 * 2, 100 * 2 + 9900 * 3, 100 * 2 + 9900 * 3 + 990000 * 5]
    if cost <= 200:
        return cost // 2
    if cost <= 30000:
        return 100 + (cost - costs[0]) // 3
    if cost <= 5000000:
        return 10000 + (cost - costs[1]) // 5
    
    return 1000000 + (cost - cost[2]) // 7


def get_cost(wh):
    usage_wh = [100, 10000, 1000000]
    costs = [100 * 2, 100 * 2 + 9900 * 3, 100 * 2 + 9900 * 3 + 990000 * 5]
    
    if wh < usage_wh[0]:
        return 2 * wh
    if wh < usage_wh[1]:
        return costs[0] + (wh - usage_wh[0]) * 3
    if wh < usage_wh[2]:
        return costs[1] + (wh - usage_wh[1]) * 5
    
    return costs[2] + (wh - usage_wh[2]) * 7


input = sys.stdin.readline

while True:
    a, b = map(int, input().split())
    
    if a == b == 0:
        break
    
    total_wh = get_wh(a)   # 나 + 이웃 전기 사용량
    
    left = 1
    right = total_wh
    answer = 0
    while left <= right:
        my_wh = (left + right) // 2
        neighborhood_wh = total_wh - my_wh
        
        my_cost = get_cost(my_wh)
        neighborhood_cost =  get_cost(neighborhood_wh)
        diff = neighborhood_cost - my_cost
        
        if diff == b:
            answer = my_cost
            break
        
        if diff > b:
            left = my_wh + 1
        else:
            right = my_wh - 1

    print(answer)
