# 백준 26042번

# 입력
# 첫 번째 줄에 n이 주어진다.
# 두 번째 줄부터 n개의 줄에 걸쳐 한 줄에 하나의 정보가 주어진다. 주어지는 정보는 유형 1, 2중 하나이다.

# 로직
# m[0] == 1 이면 줄을 선 학생의 번호 deque에 담기
# 그리고 count + 1
# m[1] == 2 이면 popleft() - 밥 먹으러감
# 그리고 count - 1
# 학생 수가 최대가 되었던 순간 -> 로직을 어떻게 짤지 모르겠음

# 출력
# 식당 입구에 줄을 서서 대기하는 학생 수가 최대가 되었던 순간의 학생 수 - 
# 식당 입구의 맨 뒤에 대기 중인 학생의 번호를 빈칸을 사이에 두고 순서대로 출력 
# 대기하는 학생 수가 최대인 경우가 여러 번이라면  / 맨 뒤에 줄 서 있는 학생의 번호가 가장 작은 경우를 출력 

input = __import__('sys').stdin.readline

n = int(input())
stack = []	#현재 대기줄
maxs = [0,0]
for _ in range(n):
    info = list(map(int,input().split()))	#입력
    if len(info) == 1:	#입력이 2라면?
        stack.pop(0)	#식사가 준비되었으니 현재 대기줄 맨 앞에 있는 인원을 제거해준다
    else:	#아니라면 마지막에 줄을 세운다
        stack.append(info[1])

    if maxs[0] < len(stack):	#현재 줄에 최대 인원이 있다면 갱신해준다
        maxs[0] = len(stack)
        maxs[1] = stack[-1]
    elif maxs[0] == len(stack):	#현재 줄에 인원이 최대라면? 마지막 인원이 작은 값을 취해준다
        maxs[1] = min(maxs[1],stack[-1])

print(maxs[0],maxs[1])
