"""
입력한 수를 이진수를 바꿨을 때, 1의 개수만 카운팅하면 된다.
"""
x = int(input())
print(bin(x).count('1'))
