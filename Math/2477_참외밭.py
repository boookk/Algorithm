k = int(input())
arr = [list(map(int, input().split())) for _ in range(6)]

w = w_idx = 0
h = h_idx = 0 

for i in range(6):
    if arr[i][0] == 1 or arr[i][0] == 2:
        if w < arr[i][1]:
            w = arr[i][1]
            w_idx = i
    else:
        if h < arr[i][1]:
            h = arr[i][1]
            h_idx = i

sub_w = abs(arr[(w_idx - 1) % 6][1] - arr[(w_idx + 1) % 6][1])
sub_h = abs(arr[(h_idx - 1) % 6][1] - arr[(h_idx + 1) % 6][1])
answer = (w * h - (sub_w * sub_h)) * k

print(answer)
