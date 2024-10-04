# 백준 16466번

# 입력
# 첫째 줄에 1차 티켓팅에서 팔린 티켓들의 수인 정수 N
# 둘째 줄에는 1차 티켓팅에서 팔린 티켓들의 번호 정수 A

# 출력
# 2차 티켓팅에서 양한이가 가질 수 있는 티켓 중 가장 작은 번호를 출력

# 로직
# 1. 티켓팅에서 팔린 티켓 입력받음
# 2. 이미 팔린 티켓을 담는 배열 만듬
# 3. 팔린 티켓 입력 받음
# 4. 입력 받은 티켓 배열에 담아줌
# 5. 티켓 번호를 나타내는 변수 생성(1부터 시작)
# 6. 반복문으로 ticket 여부 확인
# 7. 있으면 티켓 번호 증가
# 8. 티켓 출력

from sys import stdin

n = int(stdin.readline())
a = list(map(int, stdin.readline().split()))
a.sort()
ticket = 1
  
for i in range(len(a)):
  if a[i] == ticket:
    ticket += 1

print(ticket)

