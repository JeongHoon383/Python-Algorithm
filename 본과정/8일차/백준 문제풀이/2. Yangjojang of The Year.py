# 백준 11557번

# 입력
# 첫 줄 테스트 케이스 T
# 매 입력의 첫 줄 대학교의 수 N
# N 줄부터 대학교 이름, 술 소비량 공백 기준으로 입력

# 출력
# 술 소비량 많은 대학교 출력

# 로직
# 1. 테스트 케이스 for 문
# 2. 대학교, 술 소비량으로 묶어서 배열에 저장
# 3. 소비량 기준으로 내림차순 정렬
# 4. 소비량 제일 많은 대학교 출력

t = int(input())

for _ in range(t):
  n = int(input())
  university = [ [int(num), u] for u, num in (input().split() for _ in range(n)) ]
  university.sort(reverse=True)
  print(university[0][1])




