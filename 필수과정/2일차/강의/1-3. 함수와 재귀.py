def pass_by_default (a, b):
  print(a, b)
  print(a+b)

pass_by_default(b=1, a=3) # 키워드에 맞춰서 값 전달

def pass_by_pos(a, b, /) : # 오직 위치 기준으로 전달
  print(a, b)

# pass_by_pos(a=2, b=3) # 에러

def pass_by_kwrg (*, a, b): # 오직 키워드 기준으로 전달
  print(a, b)

pass_by_kwrg(b=3, a=2) 
# pass_by_kwrg(3, 2) # 에러

def test(a, b):
  a = "bcd"
  # b = [1, 2, 3] 다른 리스트 선언시 원래 y 값이 나옴
  # why? b가 가리키고 있는 원래 y값과 연결성이 끊어짐
  # 새로운 값으로 연결되어지고 함수 밖에서 만든 y값과는 관련성이 없어짐
  b[0] = "4"

x = "abc"
y = ['a', 'b', 'c']
test(x, y)

# 뭐가 먼저지?

print(x,y) # y값 리스트에 영향 있음.

## 재귀
def factorial(n):
  if n == 1:
    return 1
  return n * factorial(n-1)
print(factorial(5))
