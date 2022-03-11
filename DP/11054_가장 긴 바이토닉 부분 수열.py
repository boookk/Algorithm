"""
원본 리스트에서 증가하는 가장 긴 부분 수열과 뒤집은 리스트에서 감소하는 가장 긴 부분 수열을 구한다.
증가하는 가장 긴 부분 수열의 i번째 값과 감소하는 가장 긴 부분 수열의 n - i - 1 번째 값을 더한 후 1을 빼면 바이토닉 부분 수열의 길이가 나온다.
그 중 가장 큰 값을 출력하면 된다.
"""
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
reverse_arr = arr[::-1]
inc = [1] * n
dec = [1] * n
for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]:
            inc[i] = max(inc[i], inc[j] + 1)
        if reverse_arr[i] > reverse_arr[j]:
            dec[i] = max(dec[i], dec[j] + 1)

result = 0
for i in range(n):
    result = max(result, inc[i] + dec[n - i - 1] - 1)
print(result)
