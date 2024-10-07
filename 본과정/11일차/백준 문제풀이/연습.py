from collections import deque
import sys
input = sys.stdin.readline

# 입력 받기
# n: 도시의 개수, m: 도로의 개수, k: 거리 정보, x: 출발 도시 번호
n, m, k, x = map(int, input().split())

# 각 도시를 연결하는 그래프 (도시 번호는 1부터 시작하므로 n+1)
# 정보를 저장하는 역할
graph = [[] for _ in range(n+1)]

# 각 도시 최단 거리를 계산하는 리스트
distance = [0] * (n+1)

# 방문 횟수
visited = [False] * (n+1)

for _ in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)

def bsf(start):
  answer = [] # 최단거리 이동한 도시를 저장하는 리스트

  q = deque([start]) # 실제 이동하는 큐

  visited[start] = True # 첫 방문 도시는 방문 처리
  distance[start] = 0

  while q:
    now = q.popleft() # 현재 도시 

    for i in graph[now]: # 
      if not answer[i] :
        

