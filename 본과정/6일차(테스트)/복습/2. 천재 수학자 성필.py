# 백준 15815번

# 입력
# 길이가 100이 넘지 않는 수식이 예제 입력과 같이 공백 없이 입력
# 수식은 0부터 9까지의 숫자와 연산자 '+', '-', '*', '/' 로만 이루어져 있다.

# 출력
# 성필의 수식의 답 출력

# 로직
# 1. 맨 오른쪽의 연산자를 첫번째 요소 오른쪽에 배치
# 2. 두번째 연산자를 왼쪽으로 한칸 이동
# 3. 완성된 수식 계산

from collections import deque

n = input() # 123*+
stack = deque()

for i in n: # str 하나씩 쪼갬
    if i.isdigit():  # 숫자인 경우 스택에 추가
        stack.append(int(i)) # stack = [1, 2, 3]
    else:  # 연산자를 만난 경우
        b = stack.pop()  # 스택에서 두 번째 피연산자 꺼내기, b = 3, 6
        a = stack.pop()  # 스택에서 첫 번째 피연산자 꺼내기  a = 2, 1
        # 연산 수행, stack = [1, 6], []
        if i == '+':
            stack.append(a + b)
        elif i == '-':
            stack.append(a - b)
        elif i == '*':
            stack.append(a * b)
        elif i == '/':
            stack.append(a // b)  # 문제에서 정수 나눗셈으로 요구
# 최종 결과 출력
print(stack.pop())

# from collections import deque

# n = input()
# d = deque(n)
# list_ = []

# while(len(d) > 0):
#   if(d[-1] in ['+', '-', '*', '/']):
#     list_.append(d.popleft())
#     if len(d) > 0:
#       list_.append(d.pop()) 
#   else: list_.append(d.pop())

# print(eval(''.join(list_)))

# # 답은 나오는데 틀림
# # 접근 방식 자체가 내가 이상한건지 
# # 예외 상황을 고려하지 않고 문제만 해결하려고 해서 그런가?
# # 예외 상황을 어떻게 고려하고 로직을 짜야하는지


