# 백준 2210번

# 입력
# 5 * 5 숫자판 입력

# 출력
# 서로 다른 여섯자리의 수들의 개수 구하기

# 로직
# 모든 여섯자리의 경우의 수
# 

# 문제
# 입력부터 막힘, 숫자판 어떻게 입력받음

from sys import stdin

def dfs(x, y, number):
    # 현재 좌표 (x, y)에서 6자리 숫자를 만드는 깊이 우선 탐색 (DFS) 함수
    if len(number) == 6:  # 만약 6자리 숫자가 만들어졌다면
        if number not in result:  # result에 없는 숫자라면
            result.append(number)  # result 리스트에 추가
        return  # 겹치는 번호가 있으면 탐색 종료

    # 상하좌우 방향으로 이동하기 위한 x, y 좌표 변화 값
    dx = [1, -1, 0, 0]  # 상하좌우로 이동하는 x 방향
    dy = [0, 0, 1, -1]  # 상하좌우로 이동하는 y 방향
    # 여기까지는 어찌저찌 이해함

    # 네 방향(상하좌우)으로 이동을 시도
    for k in range(4): # 0, 1, 2, 3
        ddx = x + dx[k]  # 이동한 새로운 x 좌표
        ddy = y + dy[k]  # 이동한 새로운 y 좌표
        # 새로운 좌표가 5x5 배열의 범위 내에 있을 때만 이동 가능
        if 0 <= ddx < 5 and 0 <= ddy < 5:  
            # 새로운 좌표에서의 숫자를 추가하고, 재귀적으로 다음 단계 탐색
            dfs(ddx, ddy, number + matrix[ddx][ddy])
# 입력: 5x5 크기의 매트릭스를 문자열로 받음
matrix = [list(map(str, stdin.readline().split())) for _ in range(5)]
# 6자리 숫자를 저장할 리스트
result = []
# 5x5 배열의 모든 좌표에서 탐색 시작
for i in range(5):
    for j in range(5):
        dfs(i, j, matrix[i][j])  # 좌표 (i, j)에서 시작하는 6자리 숫자 생성
print(len(result))# 결과로 만들어진 6자리 숫자의 개수를 출력