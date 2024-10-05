# 백준 13975번

# 입력
# 첫 째줄 T개의 테스트 데이터 n 
# 테스트 데이터 첫 째 줄에는 소설을 구성하는 장의 수 m 
# 둘째 줄에는 1장부터 m장까지의 크기를 나타내는 양의 정수가 주어짐

# 로직
# 정수 리스트에 담아주기
# 제일 작은 두개 합치기 그리고 두개 합친 값 다시 heapq에 넣기

# 출력
# 최소비용 출력

import heapq

T = int(input())
for _ in range(T):
  K = int(input()) # 소설 장의 수
  files = list(map(int, input().split())) # 소설의 장의 크기
  heapq.heapify(files) 
  answer = 0

  while len(files) > 1:
    temp = 0
    a = heapq.heappop(files) # 30, 40
    b = heapq.heappop(files) # 30, 50
    temp += a + b # 90
    answer += temp # 60 + 90  
    heapq.heappush(files, temp) # temp 까지 files에 들어가니까 배열이 추가됨
  
  print(answer)