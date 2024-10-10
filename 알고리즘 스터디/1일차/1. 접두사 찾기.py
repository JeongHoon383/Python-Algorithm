# 백준 14426번

# 입력
# 첫째 줄에 문자열의 개수 N과 M
# 다음 N개의 줄에는 집합 S에 포함되어 있는 문자열
# 다음 M개의 줄에는 검사해야 하는 문자열

# 출력
# 첫째 줄에 M개의 문자열 중에 총 몇 개가 포함되어 있는 문자열 중 적어도 하나의 접두사인지 출력

# 로직
# 접두사의 기준 - 가장 앞 부분 문자열
# 문자열 집합, 접두사 배열에 넣어주기
# 만약 m의 문자열이 n의 문자열 중 앞에서 시작하는게 있다면 접두사
# m의 문자열이 n의 문자열을 탐색해야됨
# m의 문자열이 n과 일치할때 cnt += 1

# 정렬 생각 못함
# 두 문자열을 while문으로 돌려야겠다고 생각 했는데 조건을 생각 못함

# 내풀이
# from sys import stdin
# input = stdin.readline

# n, m = map(int, input().rstrip().split())
# s = [] # 문자열 집합
# t = [] # 접두사
# cnt = 0

# for _ in range(n):
#   s.append(input().rstrip())

# for _ in range(t):
#   t.append(input().rstrip)

import sys
input = sys.stdin.readline

if __name__ == "__main__":
  n, m = map(int, input().split())
  S = []
  for _ in range(n):
    S.append(input().strip()) # S에 포함되어 있는 문자열
  S.sort() # ['baekjoononlinejudge', 'codeplus', 'codingsh', 'startlink', 'sundaycoding']
  answer = 0
  s = [] # 검사해야 할 문자열
  for i in range(m):
    test = input().rstrip()
    s.append(test)
  s.sort() # ['baekjoon', 'cod', 'code', 'coding', 'judge', 'online', 'plus', 'star', 'start', 'sunday']
  i = 0 # 문자열 리스트 S의 인덱스 i
  j = 0 # 검사할 문자열 리스트 s의 인덱스 j
  while i<n and j<m: # S와 s를 모두 탐색하는 동안 반복 (S의 크기 n, s의 크기 m)
    if S[i][:len(s[j])] == s[j]: # S[i]의 앞부분이 s[j]와 같은지 확인
      answer += 1 # 접두사가 일치하면 answer 증가
      j += 1 # 다음 검사할 문자열로 이동
      continue # 다음 루프로 넘김
    elif S[i] > s[j]: #만약 S[i]가 사전순으로 s[j]보다 크다면
      j += 1 # s[j]보다 더 큰 값이므로, s[j]를 건너뛰고 다음 검사할 문자열로 이동
      continue
    elif S[i] < s[j]: # 만약 S[i]가 사전순으로 s[j]보다 작다면
      i += 1 # S[i]보다 더 큰 s[j]를 검사해야 하므로, S[i]를 건너뛰고 다음 문자열로 이동
      continue
  print(answer)

  # 41956KB, 92ms





