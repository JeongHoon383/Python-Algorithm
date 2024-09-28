# 문제 분석
# 모든 단어의 길이가 홀수
# 비밀번호가 "tulipan"인 경우에 목록에는 "napilut"도 존재해야 한다.
# 비밀번호의 길이와 가운데 글자를 출력하는 프로그램을 작성

# 로직
# 비밀번호가 무엇인지 알아내야함
# 각 단어를 리스트에 저장 - o 
# 비밀번호를 저장 할 리스트 생성 - o
# 단어가 있는 리스트를 순회하면서 뒤집은 값이 있는지 확인 ex) 0번째 확인할 때 0번째를 뒤집고 n번째 순회
# 비밀번호를 찾으면 비밀번호 리스트에 추가
# 비밀번호의 길이와 가운데 글자 출력

# 입력
# 첫째 줄에 단어의 수 N
# 다음 N개 줄에는 파일에 적혀있는 단어가 한 줄에 하나씩 주어진다.

# 출력
# 첫째 줄에 비밀번호의 길이와 가운데 글자를 출력

# 어려웠던 부분
# 문법이 너무 헷갈림
# 가운데 단어 출력하는 방법
# 숫자랑 단어 공백 있게 문자열로 출력하는 방법

N = int(input())
wordList = [] # 단어를 담아주는 리스트
password = [] # 정답 비밀번호

# list에 단어 담아주기
for _ in range(N):
  words = input().rstrip()
  wordList.append(words)

# 비밀번호가 있는지 체크
for word in wordList:
  reversed_word = word[::-1] # 리스트에 있는 단어 뒤집음
  if reversed_word in wordList: # 뒤집은 단어가 리스트에 있으면 비밀번호임
    password.append(word) 

mid = len(password[0])//2 # 단어가 홀수이므로 2로 나눠주면 가운데 값을 알 수 있음

print(f"{len(password[0])} {password[0][mid]}")

