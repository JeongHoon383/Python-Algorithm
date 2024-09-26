# 문제 분석
# 1. 높이만 다르고 (같은 높이의 막대기가 있을 수 있음) 모양이 같은 막대기를 일렬로 세운다.
# 2. 일렬로 세운 막대기를 왼쪽부터 차례로 번호를 붙인다.
# 3. 일렬로 세워진 막대기를 오른쪽에서 보면 보이는 막대기가 있고 보이지 않는 막대기가 있다.
# 4. 즉, 지금 보이는 막대기보다 뒤에 있고 높이가 높은 것이 보이게 된다.
# 5. N개의 막대기에 대한 높이 정보가 주어질 때, 오른쪽에서 보아서 몇 개가 보이는지를 알아내는 프로그램

# 로직
# 1. stack에 입력 값 다 채움
# 2. stack에 개수만큼 반복문 돌림
# 3. stack 맨 마지막 값보다 큰 값들은 pop, pop 했을 때 answer 값 올려주기

# 입력
# 1. 첫 번째 줄에는 막대기의 개수를 나타내는 정수 N이 주어짐
# 2. N줄 각각에는 막대기의 높이를 나타내는 정수 h가 주어짐

# 궁금한 점
# 반복문을 2번 돌리지 않고 푸는 방법은 없을까?

from sys import stdin
N = int(stdin.readline())

stack = []
MaxHeight = 0 # 높이가 가장 큰 막대기, 기준이 되는 막대기
answer = 0 # 보이는 막대기 수

for _ in range(N):
  h = int(stdin.readline())
  stack.append(h)
  # 막대기 개수만큼 반복문 실행, 막대기의 높이 stack에 입력
  
for _ in range(len(stack)):
  if(stack[-1] > MaxHeight): # stack에 마지막 값이 가장 크다면
    MaxHeight = stack[-1] # MaxHeight에 담아줌
    stack.pop() # 마지막 값 제거
    answer += 1 # MaxHeight에 담기는 시점에 answer 값 증가 why? 값이 가장 크면 막대기를 볼 수 있음
  else : stack.pop() # MaxHeight 보다 높이가 작을때 stack 에서 제거

print(answer)

