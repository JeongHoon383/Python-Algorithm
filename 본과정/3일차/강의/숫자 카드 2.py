# 문제 분석
# 정수 하나가 적혀져 있는 숫자 카드 주어짐
# 숫자 카드 N개를 갖고 있음
# 정수 M이 적혀있는 숫자 카드를 몇개 가지고 있는가?

# 로직
# 딕셔너리에 키가 존재하면 값으로 count를 넣어줌 why? 각 요소가 몇개가 있는지 확인
# 개수를 구해야 할 숫자를 딕셔너리에서 찾아서 값을 꺼내줌

# 입력
# 첫째 줄에는 숫자 카드 개수 N
# 둘째 줄에는 숫자 카드에 적혀있는 정수
# 셋재 줄에는 M이라는 숫자
# 넷째 줄에는 개수를 구해야 할 숫자가 적혀있음

# N 입력 및 카드 리스트 입력
N = int(input())
cards = list(map(int, input().split()))

# M 입력 및 쿼리 리스트 입력
M = int(input())
queries = list(map(int, input().split()))

# 카드 개수를 세기 위한 딕셔너리
card_count = {}
for card in cards:
  if card in card_count:
    card_count[card] += 1
  else:
    card_count[card] = 1

# 각 쿼리에 대한 결과 계산
result = []
for query in queries:
  result.append(str(card_count.get(query, 0)))

# 결과 출력
print(" ".join(result))

