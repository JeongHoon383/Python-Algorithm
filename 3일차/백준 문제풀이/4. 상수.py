a, b = input().split() # 입력 값을 공백을 기준으로 나눔, ex) 3 5 -> ['3', '5'], a = 3, b = 5

a = int(a[::-1]) # [::-1] : 문자열 또는 배열 의 요소를 뒤집음
b = int(b[::-1]) # 문자열을 뒤집고 다시 정수로 변환

if a > b:
  print(a)
else : 
  print(b)
