import sys

n, m = map(int, input().split())
result = []
people = {}
for _ in range(n):
    people[sys.stdin.readline().rstrip()] = 1

for _ in range(m):
    person = sys.stdin.readline().rstrip()
    tmp = people.get(person)
    if tmp:
        result.append(person)

print(len(result))
print(*sorted(result), sep='\n')
