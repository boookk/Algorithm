import sys
input = sys.stdin.readline


def combinations(arr, r, depth):
    if r == 0:
        print(*arr)
    elif depth == k:
        return
    else:
        combinations(arr + [numbers[depth]], r - 1, depth + 1)
        combinations(arr, r, depth + 1)


while True:
    numbers = list(map(int, input().split()))
    
    if numbers[0] == 0:
        break
    
    k = numbers[0]
    numbers = numbers[1:]
    combinations([], 6, 0)
    print()
