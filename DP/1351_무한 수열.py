"""
DP 문제였으나, 리스트로 하면 시간 초과가 발생하기 때문에 딕셔너리를 이용하여 문제를 해결했다.
"""
def dfs(num):
    if dp_dict.get(num):
        return dp_dict[num]
    
    dp_dict[num] = dfs(num // p) + dfs(num // q)
    
    return dp_dict[num]

n, p, q = map(int, input().split())

dp_dict = {0: 1}

print(dfs(n))
