# 백준 7562번

# 입력
# 첫째 줄에는 테스트 케이스의 개수
# 테스크 케이스의 첫째 줄에는 체스판의 한 변의 길이 L (L * L)
# 둘째 줄 나이트가 현재 있는 칸
# 셋째 줄 나이트가 이동하려는 칸

# 출력
# 각 테스트 케이스마다 나이트가 최소 몇 번만에 이동할 수 있는지

# 로직
# 1. 체스판의 크기와 시작점, 도착점을 입력받음
# 2. BFS를 통해 각 지점을 방문하면서, 나이트가 이동할 수 있는 모든 방향으로 이동
# 3. 도착점에 도달하면 그 지점까지 이동한 횟수를 반환

# 이해 안되는 부분
# 체스판의 각 칸은 두 수의 쌍

from collections import deque
import sys
input = sys.stdin.readline

# 테스트 케이스 수를 입력 받음
t = int(input().rstrip())

# BFS 함수 정의
def bfs():
    # 나이트가 이동할 수 있는 8가지 방향 설정
    dx = [-1, 1, 2, 2, 1, -1, -2, -2]
    dy = [2, 2, 1, -1, -2, -2, -1, 1]

    # BFS 탐색을 위한 큐 선언, 시작점 추가
    q = deque()
    q.append((startX, startY))
    
    # 큐가 빌 때까지 탐색을 진행
    while q:
        # 큐에서 좌표를 하나 꺼냄
        x, y = q.popleft()
        
        # 만약 현재 위치가 목표 지점이면, 이동 횟수를 반환
        if x == endX and y == endY:
            return matrix[x][y] - 1  # 시작점이 1로 설정되어 있어 -1 해줌
        
        # 나이트가 이동할 수 있는 8가지 방향에 대해 탐색
        for i in range(8):
            nx = x + dx[i]  # 새로운 x 좌표
            ny = y + dy[i]  # 새로운 y 좌표
            
            # 새로운 좌표가 체스판 안에 있고, 아직 방문하지 않은 좌표일 경우
            if 0 <= nx < l and 0 <= ny < l and matrix[nx][ny] == 0:
                matrix[nx][ny] = matrix[x][y] + 1  # 이동 횟수 증가
                q.append((nx, ny))  # 큐에 새로운 좌표 추가

# 각 테스트 케이스에 대해 실행
for _ in range(t):
    l = int(input().rstrip())  # 체스판의 크기 입력
    startX, startY = map(int, input().rstrip().split())  # 시작점 좌표 입력
    endX, endY = map(int, input().rstrip().split())  # 목표점 좌표 입력
    
    # 체스판을 0으로 초기화, 나이트의 이동 경로를 기록할 행렬
    matrix = [[0] * l for _ in range(l)] # -> 이부분 틀림 x * x 체스판 만들어줄 때 요소를 길이만큼 곱해주고 거기에 길이만큼 for문을 돌려줄 것, 이중for문 아님
    matrix[startX][startY] = 1  # 시작점을 1로 설정 (이동 횟수 계산을 위해)
    
    # BFS 탐색 결과 출력
    print(bfs())

# 34088KB, 1096ms


# 내 풀이, 로직 어떻게 짜야할지 모르겠음
# n = int(input()) # 테스트 케이스
# L = int(input()) # 체스 변의 길이

# for _ in range(n):
#   graph = [[] for _ in range(L) for _ in range(L)]
#   visited = [[false] for _ in range(L) for _ in range(L)] # 방문여부 확인
#   moved = [] # 이동 횟수 저장하는 리스트