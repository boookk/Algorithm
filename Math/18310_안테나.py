n = int(input())
locations = list(map(int, input().split()))

locations.sort()

print(locations[(n - 1) // 2])
