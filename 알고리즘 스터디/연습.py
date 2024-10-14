n = input(input())
top = list(map(int, input().split()))
stack = [] # 탑의 인덱스, 탑의 높이를 쌍으로 저장
answer = [0 for i in range(n)] # 레이저 신호를 수신한 탑들의 번호

for i in range(n):
  while stack : # 스택이 존재할때까지 반복문 실행
    if stack[-1][1] > top[i]: # 가장 끝 탑의 높이가 현재 탑보다 높으면
      answer[i] = stack[-1][0] + 1 
      # 스택에 있는 탑의 인덱스는 0부터 시작하므로, 1을 더하여 based index로 변환해 기록
      break
      # 레이저가 닿은 탑을 찾았으므로 더 이상 비교할 필요가 없어 반복문을 종료
    else:
      stack.pop()
      # 현재 탑보다 작은 탑은 레이저에 가려지므로, 스택에서 제거

  stack.append([i], top[i])
  # 현재 탑의 인덱스와 높이를 스택에 추가하여 다음 탑과의 비교를 준비

print(*answer) 