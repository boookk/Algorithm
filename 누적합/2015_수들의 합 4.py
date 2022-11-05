n, k = map(int, input().split())
lst = list(map(int, input().split()))

sum_lst = [0]
sum_dict = dict()
answer = 0

for val in lst:
    sum_lst.append(sum_lst[-1] + val)

for i in range(n + 1):
    answer += sum_dict.get(sum_lst[i] - k, 0)
    sum_dict[sum_lst[i]] = sum_dict.get(sum_lst[i], 0) + 1

print(answer)
