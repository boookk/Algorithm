n, kim, im = map(int, input().split())

answer = 0

while kim != im:
    kim -= kim // 2
    im -= im // 2
    answer += 1

print(answer)
