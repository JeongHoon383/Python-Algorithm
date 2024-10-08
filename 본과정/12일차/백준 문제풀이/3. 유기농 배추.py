# 백준 1012번 

# 입력
# 첫 줄에는 테스트 케이스의 개수 T
# 다음 줄부터 각각의 테스트 케이스에 대해 첫째 줄에는 배추를 심은 배추밭의 가로길이 M, 세로길이 N, 배추가 심어져 있는 위치의 개수 K
# 그 다음 K줄에는 배추의 위치 X

# 출력
# 각 테스트 케이스에 대해 필요한 최소의 배추흰지렁이 마리 수를 출력
# 네 방향에 배추가 있는지 확인 없으면 지렁이 수 증가

# 로직
# 테스크 케이스 입력 받은 후 배추밭 생성

# 문제
# k가 왜 필요하지?

from sys import stdin
input = stdin.readline
t = int(input())

for _ in range(t):
  m, n, k = map(int, input().split())
  graph = [[] * m for _ in range(n)] # m행 n열 배추밭
  visited = [[False] * m for _ in range(n)] # 배추밭 방문 여부
  


