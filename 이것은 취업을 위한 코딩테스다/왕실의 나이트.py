location = input()
x, y = int(location[1]) - 1, ord(location[0]) - 97

direction = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
result = 0
for d in direction:
    nx, ny = d[0] + x, d[1] + y
    if -1 < nx < 8 and -1 < ny < 8:
        result += 1
print(result)
