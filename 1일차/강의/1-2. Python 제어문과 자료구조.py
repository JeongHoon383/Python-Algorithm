# a = int(input())

a = 4
if a < 3:
  print("a는 3미만 입니다.")
elif a < 5:
  print("a는 3이상 5미만")

s = "Hello"
for c in s:
  if c == "e":
    break
  print(c)

# 구구단 2단 출력하기
  for i in range(1, 10):
    print(f"2 x {i} = {2 * i}")

  for j in range(2, 10):
    print(f"---{j}단---")
    for k in range(1, 10):
      print(f"{j} * {k} = {j * k}")

a = {"name" : "hoon", "age" : 26}
print(a["name"])