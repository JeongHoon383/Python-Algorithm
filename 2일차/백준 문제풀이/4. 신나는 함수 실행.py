# 다차원 배열 dp를 사용해 재귀적으로 값을 계산하는 동적 프로그래밍(DP) 방식의 문제
# 주어진 입력 값에 따라 w(a, b, c) 를 계산하여 결과를 출력

import sys # 표준 라이브러리 sys를 가져옴 (입력 처리를 빠르게 하기 위함)

# 입력을 빠르게 받기 위한 설정 (sys.stdin.readline은 한 줄씩 입력 받음)
sysInput = sys.stdin.readline

# 21x21x21 크기의 3차원 리스트 dp 선언. 각 값을 0으로 초기화
# dp[a][b][c]는 w(a, b, c)의 값을 저장해 중복 계산을 방지
dp = [[[0 for _ in range(21)] for _ in range(21)] for _ in range(21)]

# 동적 계획법(DP)을 이용하여 w(a, b, c)를 계산하는 함수
def DP(a, b, c):
  # a, b, c 중 하나라도 0 이하이면 1을 반환
  if a <= 0 or b <=0 or c<= 0:
    return 1
  # a, b, c 중 하나라도 20을 초과하면 w(20, 20, 20)을 계산
  if a > 20 or b > 20 or c > 20:
    return DP(20, 20, 20)
  # dp[a][b][c]에 이미 값이 저장되어 있으면 해당 값을 반환(중복 계산 방지)
  if dp[a][b][c]:
    return dp[a][b][c]
  # a < b < c 조건을 만족할 때 재귀적으로 값을 계산
  if (a < b < c) :
    # w(a, b, c) = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
    dp[a][b][c] = DP(a, b, c-1) + DP(a, b-1, c-1) - DP(a, b-1, c)
    return dp[a][b][c]
  else:
    # 그렇지 않으면 다른 재귀 규칙에 따라 값을 계산
    # w(a, b, c) = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
    dp[a][b][c] = DP(a-1, b, c) + DP(a-1, b-1, c) + DP(a-1, b, c-1) - DP(a-1, b-1, c-1)
    return dp[a][b][c]
  
# 무한 루프를 통해 입력을 반복해서 받음
while(True):
  # 입력을 받아서 a, b, c로 나눔 (map(int, ...)을 통해 문자열을 정수로 변환)
  a, b, c = map(int, sysInput().split())
  # 입력이 (-1, -1, -1)일 경우 반복을 종료
  if(a, b, c) == (-1, -1, -1):
    break
  print("w({}, {}, {}) = {}".format(a, b, c, DP(a, b, c)))

