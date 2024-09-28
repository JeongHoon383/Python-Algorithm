# 문제 분석
# 득표수가 제일 많을 때 당선이 됨
# 나보다 많은 득표수를 가진 사람의 둑표수를 줄이고 내 득표수를 올림
# 줄여야 할 득표수의 최솟값은? 

# 로직
# 후보 : 득표수 와 같은 쌍을 가진 딕셔너리 생성
# 1번 후보와 다음 후보 비교
## 1번 후보의 득표수가 늘어날 때 득표수를 체크할 count++
## 만약 다음 후보가 득표수가 1번과 같거나 많다면? : 1번 득표수 ++, 다음 후보 득표수 --
## 만약 다음 후보가 득표수가 1번보다 적다면? : 다다음 후보로 넘어감
# 다음 후보가 없다면 종료. 득표수 출력

# 입력
# 첫째 줄에 후보의 수 N
# 둘째 줄부터 차례대로 기호 1번을 찍으려고 하는 사람의 수, 기호 2번을 찍으려고 하는 수, 이렇게 총 N개의 줄

# 출력
# 매수해야 하는 사람의 최솟값

import sys, heapq  
input = sys.stdin.readline  

n = int(input())  # 후보자의 수 n을 입력받음
win = int(input())  # 1번 후보의 득표수 입력 받음
nums = []  # 득표수를 저장할 빈 리스트 생성

# n - 1명의 득표수를 입력받아 우선순위 큐에 저장
for _ in range(n - 1):
    num = int(input())  # 각 후보의 득표수를 입력받음
    heapq.heappush(nums, (-num, num))  # 득표수를 음수로 변환하여 최소 힙을 최대 힙처럼 사용하기 위해 저장
    # heapq는 기본적으로 최소 힙 자료구조이기 때문에 음수로 만들어야 최대 힙처럼 사용할 수 있음.
    # -num 을 넣어줌으로써 heapq에 (음수, 양수) 이렇게 저장되고
    # 최소 힙 자료구조 특성상 가장 작은 값이 반환되지만 실제 값을 같이 넣어줌으로써 최대 값 처럼 사용할 수 있는 것

cnt = 0  
while nums:  # nums에 득표수가 남아있는 동안 반복
    num = heapq.heappop(nums)[1]  # 힙에서 가장 큰 득표수를 가져옴 (음수로 저장했으므로 음수를 제거한 값)
    
    if num >= win:  # 현재 득표수가 이긴 후보의 득표수보다 크거나 같으면
        num -= 1  # 득표수를 1 감소시킴
        win += 1  # 이긴 후보의 득표수를 1 증가시킴
        cnt += 1  # 매수해야 하는 사람의 수 1 증가시킴
        heapq.heappush(nums, (-num, num))  # 수정된 득표수를 다시 힙에 추가

print(cnt)


# # 문제
# # 문법을 모름
# # 값이 같거나 클 때 1번 후보를 더해주고 다른 후보를 빼주게 되면 count가 하나 더 늘어나게 됨
# # 만약 4 6 6 라면 count가 3이 추가됨 근데 두번째 후보와 세번째 후보의 값을 하나씩만 빼주면 6 5 5 로 2번만 처리할 수 있음
# # 같을 때 1을 무조건 추가하면 안됨. 같을 때 만약 다음 후보가 나보다 크면 그 후보의 투표를 줄임
# # 근데 만약 모든 후보가 동일하다면? 마지막 같은 후보의 투표수를 빼주고 내 투표수를 증가
# 다솜의 득표수와 다른 후보의 득표가 같았을 때 다른 후보를 다시 비교하는 과정에서 막힘

# n = int(input())
# candidate = {}
# count = 0

# for i in range(1, n + 1):
#   m = int(input())
#   candidate[i] = m

# if len(set(candidate.values())) == 1 and len(candidate) > 1:
#   count += 1
# # 1번 후보는 고정되어 있고 1번 보다 크거나 같으면 + -, 1번 보다 작으면 count 출력
# for i in range(2, n + 1):
#   while candidate[1] < candidate[i]:
#     candidate[1] += 1
#     candidate[i] -= 1
#     count += 1
#     if(candidate[1] == candidate[i]):
#       for j in range(2, n + 1):
#         if(candidate[j] > candidate[1]):
#           candidate[1] += 1
#           candidate[j] -= 1
#           count += 1
#           break

# print(count)


