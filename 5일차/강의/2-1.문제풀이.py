def parenthesis_verification(s):
  stack = []

  for c in s:
    if c == "(":
      stack.append(c)
    elif c == ")":
      if len(stack) == 0:
        return False
      stack.pop()
  
  return len(stack) == 0 # True인지 False 인지 마지막 유효성 검사

n = int(input())
result = []

for i in range(n):
  target = input()
  result.append("YES" if parenthesis_verification(target) else "NO")

for result in result:
  print(result)