import sys
input = sys.stdin.readline # 입력 시간초과를 방지하기 위해 input을 sys함수로 대체

def recursion(s, l, r):
  global cnt
  cnt += 1

  if l >= r : return 1
  elif s[l] != s[r] : return 0
  else : return recursion(s, l+1, r-1)

def isPalindrome(s) : 
  return recursion(s, 0, len(s) - 1)

for _ in range(int(input())):
  cnt = 0 # 재귀 호출 횟수를 저장할 전역 변수 초기화
  print(isPalindrome(input().rstrip()), cnt)
    

    
