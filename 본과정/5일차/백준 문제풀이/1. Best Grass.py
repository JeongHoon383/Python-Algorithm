# 문제 분석
# # -> 풀 덩어리
# 가로로 풀 덩어리가 겹치면 count 안올라감
# 세로로 풀 덩어리가 겹치면 count 안올라감

# 입력
# 행 R : 5, 열 C : 6
# 풀과 덩어리 받기

# 로직
# 풀 리스트 입력 받기
# 행, 열 반복문
# # 일때 count + 1 다만, 같은 행에 #이 붙어있으면 count 증가 x
# 같은 열에 #이 붙어있으면 count 증가 x

# 출력
# Bessie가 먹을 수 있는 풀 덩어리 수

# 문제
# index가 범위 바깥으로 넘어갔을 때 예외처리 어떻게?
# 0일 때 조건을 추가로 붙여줄 것

r, c = map(int, input().split())  # r - 행, c - 열
grassList = []
count = 0

# 입력 처리
for i in range(r):
    grassList.append(list(input()))

# 판자 갯수 세기
for i in range(r): # 행
    for j in range(c): # 열
        if grassList[i][j] == "#":
            # 왼쪽을 확인 (첫 번째 열 제외)
            if j == 0 or grassList[i][j-1] != "#":
                # 위쪽을 확인 (첫 번째 행 제외)
                if i == 0 or grassList[i-1][j] != "#":
                    count += 1

print(count)


