# 백준 1697번

# 입력
# 첫 번째 줄에 수빈이가 있는 위치 N과 동생이 있는 위치 K

# 출력
# 수빈이가 동생을 찾는 가장 빠른 시간을 출력

# 로직
# 1. 수빈, 동생 위치 받음
# 2. 그래프, 방문 여부 생성
# 3. bsf 함수 작성 (선언, 실행, 실행 후 다시 세팅)

from sys import stdin
from collections import deque

input = stdin.readline

n, k = map(int, input().split())  # 수빈이의 위치 n, 동생의 위치 k
visited = [False] * 100001  # 최대 범위가 100000이므로 범위에 맞춰 리스트 생성
distance = [0] * 100001  # 이동 거리 저장 리스트

def bfs(start):
    queue = deque([start])  # 시작 위치를 큐에 넣고 탐색 시작
    visited[start] = True  # 시작점 방문 처리
    
    while queue:
        current = queue.popleft()  # 현재 위치를 큐에서 꺼냄
        
        if current == k:  # 동생의 위치에 도착하면 거리 출력
            return distance[current]
        
        # 이동 가능한 세 가지 방향을 처리
        for next_pos in (current - 1, current + 1, current * 2):
            if 0 <= next_pos <= 100000 and not visited[next_pos]:  # 범위 내이고 아직 방문하지 않은 위치
                visited[next_pos] = True
                distance[next_pos] = distance[current] + 1  # 현재 위치까지의 거리에 +1
                queue.append(next_pos)  # 다음 탐색을 위해 큐에 넣음

print(bfs(n))

# 내 풀이
# from sys import stdin
# input = stdin.readline
# n, k = map(int, input().split())

# graph = [[] for _ in range(k + 1)]
# visited = [False] * (k + 1)

# def bsf(start):
#   # 실제 이동하는 리스트를 만들어야 되나? 
#   # 목표 지점에 가기만 하면 됨
#   # 이동하는 거리 수 저장하는 리스트 만들어야됨 - o
#   # 이동하는 방법 선언 - 이부분에서 막힘, 어떤식으로 이동을 나타내는지 -1, 1, *2 
#   # 이동하는 모든 방법 중 가장 짧은거 출력
#   answer = []
#   visited[start] = True

#   dx = []


