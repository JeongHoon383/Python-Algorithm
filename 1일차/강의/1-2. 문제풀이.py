## 주어진 리스트에서 10 이상 정수의 합계 구하기
# 출력 : 10 이상 정수의 합계는 00입니다. 
x = [1, 10, 2, 9, 43, 9, 15]
sum = 0
for v in x:
  if v >= 10 :
    sum += v

print(f"10이상 정수의 합계는 {sum}입니다.")

## 최대값 찾기
# 입력 1, 4, 10 (공백단위로 정수 여러개)
# 출력 : 최대값은 10 입니다. 
nums = input().split(' ')

max_num = 0
for num in nums : 
  if max_num < int(num) :
    max_num = int(num)

  print(f"최대값은 {max_num}입니다.")

  ## 중복 제거하기
  nums = input().split(' ')
  num_set = set()

  for num in nums:
    num_set.add(num)


  print(list(num_set))
