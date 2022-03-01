n, k = map(int, input().split())
people = list(range(1, n+1))
result = []
index = k - 1
while people:
    result.append(people.pop(index))
    if len(people) != 0:
        index = (index + (k - 1)) % len(people)

print('<' + ', '.join(map(str, result)) + '>')
