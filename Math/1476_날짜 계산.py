e, s, m = map(int, input().split())

answer = 1
e_, s_, m_ = 1, 1, 1

while True:
    if e_ == e and s_ == s and m_ == m:
        break
    
    answer += 1
    e_ = 1 if e_ == 15 else e_ + 1
    s_ = 1 if s_ == 28 else s_ + 1
    m_ = 1 if m_ == 19 else m_ + 1

print(answer)
