"""
-를 기준으로 앞뒤로 괄호로 묶으면 된다.
처음에 eval()를 사용하여 계산했었는데, Syntax error가 발생했다.
그 이유는 피연산자 앞에 0이 있는 경우를 고려하지 못했기 때문이다. (ex. "01+1")
예외의 경우를 계산하기 위해 - 연산자로 분리한 식을 다시 + 연산자로 분리하여 계산하였다.
""" 

expression = input().split('-')
sub = list(map(lambda x: sum(map(int, x.split('+'))), expression))
result = sub[0]
for i in range(1, len(sub)):
    result -= sub[i]
print(result)
