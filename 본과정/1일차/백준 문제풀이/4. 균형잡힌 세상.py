# 입력 : . 으로 끝나는 문자 열들이 들어온다고
# 로직 :
# 1. 만약에 문장에 괄호가 하나도 없으면 'yes'
# 2. 문장에 괄호가 있다 ->
# 2-1. 제대로 괄호가 열리는지 확인 -> 열리지 않았는데 닫혔다 'no'
# 2-2. 제대로 닫혔는지 확인 -> 제대로 안닫혔으면 'no'
#
# -> 리스트를 만들어서 괄호가 나올때 넣어줄건데, 넣기전에 이게 열린 괄혼지 닫힌 괄혼지 판단
# -> 만약에 문장이 끝났는데, 리스트에 괄호가 남아있다? -> 제대로 안닫힌거 -> 'no'


# 출력 : 각 문자에 괄호(대괄호 소괄호) 가 잘 열리고 닫혔는지 확인해서, 잘 되 있으면, yes, 안되있으면 no

from sys import stdin
strings = []

# 무한 루프를 돌며 문자열 입력을 받음
while True:
  input_str = stdin.readline().rstrip()  # 개행 문자를 제거한 한 줄을 입력받음
  if input_str == '.':  # 입력이 '.'이면 종료
    break
  strings.append(input_str)  # 입력된 문자열을 리스트에 추가

# 입력된 모든 문자열에 대해 반복
for string in strings:
  check = []  # 괄호를 저장하는 리스트 (열린 괄호 관리)
  result = 'yes'  # 초기 결과값을 'yes'로 설정 (균형 잡힌 문자열로 가정)
  
  # 각 문자열을 한 문자씩 검사
  for s in string:
    if s == '(' or s == '[':  # 열린 괄호가 나오면
      check.append(s)  # check 리스트에 추가

    elif s == ')':  # 닫힌 소괄호가 나왔을 때
      if not check or check.pop() != '(':  # 열린 괄호가 없거나 마지막이 '('가 아니면
        result = 'no'  # 괄호 짝이 맞지 않으므로 'no'로 설정
        break  # 더 이상 검사할 필요 없으니 종료
    
    elif s == ']':  # 닫힌 대괄호가 나왔을 때
      if not check or check.pop() != '[':  # 열린 괄호가 없거나 마지막이 '['가 아니면
        result = 'no'  # 괄호 짝이 맞지 않으므로 'no'로 설정
        break  # 더 이상 검사할 필요 없으니 종료

  # 반복문이 끝난 후에도 check 리스트에 열린 괄호가 남아있으면
  if len(check) > 0:
    result = 'no'  # 닫히지 않은 괄호가 있는 것이므로 'no'로 설정

  print(result)  # 결과 출력 ('yes' 또는 'no')

