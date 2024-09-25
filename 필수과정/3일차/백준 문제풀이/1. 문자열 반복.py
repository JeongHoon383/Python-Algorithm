R = int(input()) # 첫 번째 줄에서 입력받을 줄 수
data = [] # 각 줄의 데이터를 저장할 리스트

for _ in range(R):
  S = input().split()
  num = int(S[0]) # 첫 번째 값은 정수
  my_str = S[1] # 두 번째 값은 문자열
  data.append((num, my_str)) # 

for num, my_str in data:
  for v in range(len(my_str)) :
    print(my_str[v] * num, end='')
  print()






