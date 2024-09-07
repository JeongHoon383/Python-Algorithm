# 백준 2605번, 32ms

num = int(input())
lst = list(map(int, input().split())) 
alst = [n for n in range(1, num+1)] # 1~num 까지의 줄 세운 학생을 list에 담아줌, 학생들의 현재 순서

for i in range(num):
  n, t = lst[i], alst[i]
  # list[i] : i번째 학생이 앞으로 몇 칸 이동해야 하는지
  # alst[i] : i번째 학생의 번호
  for j in range(i, i-n, -1): # 학생을 앞으로 이동시키는 과정
    alst[j] = alst[j-1] # i번째 학생을 i-n 위치로 이동
  alst[i-n] = t 
print(*alst) # *는 리스트의 모든 요소를 공백으로 구분하여 출력, 리스트를 벗겨냄


