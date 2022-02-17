def dfs(queens, row):
    count = 0
    if row == n:
        return 1

    for col in range(n):
        queens[row] = col
        for i in range(row):
            if queens[row] == queens[i]:
                break
            if abs(queens[i] - col) == abs(i - row):
                break
        else:
            count += dfs(queens, row+1)
    return count


n = int(input())
queens = [0] * n
print(dfs(queens, 0))
