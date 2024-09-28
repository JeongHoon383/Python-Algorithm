# 문제 분석
# 배열에 자연수 x를 넣음
# 배열에서 가장 작은 값을 출력하고, 그 값을 배열에서 제거

# 입력
# 첫째 줄에 연산의 개수 N
# 다음 N개의 줄에는 연산에 대한 정보를 나타내는 정수 x
# 만약 x가 자연수(0이 아닌)라면 배열에 추가
# 0이라면 가장 작은 값을 출력 후 배열에서 제거

# 로직
# 1. 연산 개수를 입력 받고 개수만큼 반복문 실행
# 2. 입력받은 정수가 0이 아닐때 heap에 저장
# 3. 0일때 heap에서 최소값 제거 후 출력
# 4. 만약 heap이 빈값인 상황에서 pop을 할 경우 0을 출력

# 출력
# 0이 주어진 횟수만큼 가장 작은값 출력

# 문제를 겪은 부분
# 초기 0값을 출력하는 것 때문에 못 품
# heap에 아무것도 없을 때 indexerror가 발생
# 이 부분을 try, except 문법으로 에러가 발생했을 때 0이 출력되게 처리

from sys import stdin
import heapq

numbers = int(stdin.readline()) # 연산 개수
heap = []

#Max Heap
for _ in range(numbers):
    num = int(stdin.readline())
    if num != 0:
        heapq.heappush(heap, num) # 0이 아닐때 heap에 값 저장
    else:
        try:
            print(heapq.heappop(heap)) # 0일때 최소값 반환 후 출력
        except:
            print(0) # heappop을 했을 때 에러가 발생하면 0을 출력