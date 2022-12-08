def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)


a1, b1 = map(int, input().split())
a2, b2 = map(int, input().split())

sum_a = a1 * b2 + a2 * b1
sum_b = b1 * b2

print(sum_a // gcd(sum_a, sum_b), sum_b // gcd(sum_a, sum_b))
