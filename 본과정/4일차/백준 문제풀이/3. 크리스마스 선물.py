# 문제 분석
# 산타가 선물을 나눠줌
# 곳곳에 거점들에서 선물을 채움
# 그리고 착한 아이를 만나면 제일 가치가 있는 선물을 줌
# 아이들에게 준 선물들의 가치 출력, 줄 선물이 없으면 -1 출력

# 입력
# 첫째줄에는 아이들과 거점지를 방문한 횟수 n
# 둘째줄에는 a개의 선물 충전, 뒤 숫자들은 선물의 가치

# 로직
# n 입력 받음
# n 만큼 for문 생성
# 선물의 개수와 가치를 담는 list
# 개수를 반환, 배열에서 제거 후 list를 heap에 담아줌
# 선물의 개수가 0일 때 heap에 -1 담김
# 선물의 개수만큼 반복문 돌리고 max값 출력

# 출력
# a가 0일 때마다, 아이들에게 준 선물의 가치 출력
# 만약 줄 선물이 없으면 -1 출력


import heapq

n = int(input().rstrip())
max_heap = []

for _ in range(n):
    nums = list(map(int, input().rstrip().split()))
    presentNum = nums.pop(0)  # 선물의 개수 변수로 담아줌

    if presentNum == 0:  # 선물의 개수가 0일 때
        try:
            print(-heapq.heappop(max_heap))  # heap의 최대값 출력
        except:
            print(-1)  # heap의 요소가 없을 경우 -1 출력
    else:
        for num in nums:  # 첫 번째 요소를 제외한 나머지를 선물 추가
            heapq.heappush(max_heap, -num)  # 최대 힙을 위해 음수로 변환 - 업데이트


# 내풀이 
# else 부분에서 heap이 초기화가 되어 값이 출력이 안됨

# import heapq
# n = int(input().rstrip())

# for _ in range(n):
#   nums = list(map(int, input().rstrip().split()))
#   presentNum = nums.pop() # 선물의 개수 변수로 담아줌
#   if(presentNum == 0): # 선물의 개수가 0일 때
#     try: print(-heapq.heappop(max_heap)) # heap의 최대값 출력
#     except: print(-1) # heap의 요소가 없을 경우 -1 출력
#   else:
#     max_heap = [-num for num in nums] # 최대 힙 사용을 위해 리스트 음수로 변환
#     heapq.heapify(max_heap) # 변환된 리스트 heap으로 변환 - 초기화


