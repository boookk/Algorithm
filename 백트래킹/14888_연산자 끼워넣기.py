def dfs(depth, total, plus, sub, mul, div):
    global max_, min_
    if depth == n:
        max_ = max(max_, total)
        min_ = min(min_, total)
        return

    if plus:
        dfs(depth + 1, total + num[depth], plus - 1, sub, mul, div)
    if sub:
        dfs(depth + 1, total - num[depth], plus, sub - 1, mul, div)
    if mul:
        dfs(depth + 1, total * num[depth], plus, sub, mul - 1, div)
    if div:
        dfs(depth + 1, int(total / num[depth]), plus, sub, mul, div - 1)


n = int(input())
num = list(map(int, input().split()))
op = list(map(int, input().split()))
max_ = - 10 ** 9
min_ = 10 ** 9

dfs(1, num[0], op[0], op[1], op[2], op[3])
print(max_)
print(min_)
