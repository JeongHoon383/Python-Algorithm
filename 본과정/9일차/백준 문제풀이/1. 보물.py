# 백준 1026번

# 입력
# 첫째 줄에 N
# 둘째 줄에는 A에 있는 N개의 수가 순서대로 주어짐
# 셋째 줄에는 B에 있는 수가 순서대로 주어짐

# 출력
# s의 최솟값 출력

# 로직
# 1. N 입력 받음, 반복문
# 2. A, B 입력 받음, 배열에 저장
# 3. A, B 값 순회
# 굳이 배치 할 필요없이 A의 제일 작은 값과 B의 제일 큰 값을 곱함
# 값을 계산한 A, B 의 값을 pop()
# sum에 값을 누적

# 틀린 이유
# 인덱스의 위치를 맞추려고 함
# 값을 맞추고 리스트에서 지워주면 됨

n = int(input())

a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))

s = 0 # 누적값
for i in range(n):
    s += min(a_list) * max(b_list) # a의 제일 작은 값과 b의 제일 큰 값을 곱해서 s에 누적해서 더해줄 것
    a_list.pop(a_list.index(min(a_list))) # 계산이 된 제일 작은값 list에서 삭제
    b_list.pop(b_list.index(max(b_list))) # 계산이 된 제일 큰값 list에서 삭제

print(s)

# 31120KB, 40ms

# 내풀이
# n = int(input())
# a = list(map(int, input().split())) # [1, 1, 1, 6, 0]
# b = list(map(int, input().split())) # [2, 7, 8, 3, 1]
# a.sort() # [0, 1, 1, 1, 6]

# print(max(b))

# for i in range(n):