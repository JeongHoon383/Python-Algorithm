# 백준 10773번

# 입력
# 첫 번째 줄에 정수 K
# K개의 줄에 정수가 1개씩 주어진다
# 수가 "0" 일 경우에는 가장 최근에 쓴 수를 지우고, 아닐 경우 해당 수를 쓴다.

# 출력
# 재민이가 최종적으로 적어 낸 수의 합

# 로직
# k 만큼 반복문
# 주어진 정수 list에 담아줌
# 만약 0이라면 list에 담긴 값 반환
# 최종적으로 list에 담긴 값의 합 구하기

import sys
from collections import deque

k = int(sys.stdin.readline()) 
num = deque()  

for _ in range(k):
    n = int(sys.stdin.readline())
    if n == 0:
        num.pop()
    else:
        num.append(n)

print(sum(num))



