numbers = set(range(1, 10001))
not_self_nums = set()

for number in numbers:
    for num in str(number):
        number += int(num)
    not_self_nums.add(number)

print(*sorted(numbers - not_self_nums), sep='\n')
