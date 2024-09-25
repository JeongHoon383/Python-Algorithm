# 문제 분석
# 1. 빈 문자열을 저장한다.
# 2. 누른 횟수 입력 받기
# 3. 문자열을 저장 할 리스트 생성 why? 누가 가장 마지막으로 들어왔는지 확인해야됨
# 4. 반복문 내에서 버튼을 누른 순서와 누른 버튼에 대한 정보 입력 받기
# 5. 작업 코드에 맞춰서 deque와 리스트에 추가 및 제거
# 6. deque 요소 문자열로 바꿔서 출력

# 입력
# 첫째줄 : 버튼을 누른 횟수 N 
# 둘째줄 : N개의 줄에는 버튼을 누른 순서, 누른 버튼에 대한 정보
# 1 c : 문자열 맨 뒤에 c 가 적힌 블록 추가
# 2 c : 문자열 맨 앞에 c 가 적힌 블록 추가
# 3 : 문자열을 구서하는 블록 중 가장 나중에 추가된 블록 제거

from sys import stdin  # 표준 입력을 사용하기 위해 sys 모듈에서 stdin을 가져옵니다.
from collections import deque  # deque를 사용하기 위해 collections 모듈에서 deque를 가져옵니다.

now = deque()  # 문자열을 저장할 빈 deque 생성
n = int(stdin.readline())  # 첫 번째 줄에서 작업의 수 n을 입력 받습니다.
stack = []  # 작업의 종류를 저장할 빈 리스트 생성

# n개의 작업을 반복합니다.
for _ in range(n):
    op = list(map(str, stdin.readline().split()))  # 각 줄의 입력을 공백으로 나누어 리스트로 변환합니다.
    if op[0] == '1':  # 작업 코드가 1인 경우
        now.append(op[1])  # 문자열을 deque의 뒤쪽에 추가합니다.
        stack.append('back')  # 어떤 작업이 수행되었는지 스택에 기록합니다.
    elif op[0] == '2':  # 작업 코드가 2인 경우
        now.appendleft(op[1])  # 문자열을 deque의 앞쪽에 추가합니다.
        stack.append('front')  # 어떤 작업이 수행되었는지 스택에 기록합니다.
    else:  # 작업 코드가 3인 경우
        if stack:  # 스택이 비어있지 않을 경우
            value = stack.pop()  # 스택에서 가장 최근에 수행한 작업을 꺼냅니다.
            if value == 'back':  # 만약 최근 작업이 'back'이라면
                now.pop()  # deque의 뒤쪽에서 요소를 제거합니다.
            else:  # 최근 작업이 'front'라면
                now.popleft()  # deque의 앞쪽에서 요소를 제거합니다.

# 최종 deque의 길이를 확인합니다.
if len(now) == 0:  # deque가 비어있다면
    print('0')  # '0'을 출력합니다.
else:  # deque에 요소가 있다면
    print("".join(now))  # deque의 모든 요소를 문자열로 변환하여 출력합니다.


