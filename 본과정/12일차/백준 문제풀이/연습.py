from sys import stdin
from collections import deque

input = stdin.readline

n, k = map(int, input().split())  # 수빈이의 위치 n, 동생의 위치 k
visited = [False] * 100001  # 최대 범위가 100000이므로 범위에 맞춰 리스트 생성
distance = [0] * 100001  # 이동 거리 저장 리스트

def bfs(start):
  q = deque([start])
  visited[start] = True

  while q:
    current = q.popleft() # 현재값 추출

    if current == k:
      return distance[current]
    
    for next_pos in (current-1, current+1, current*2):
      if 0 <= next_pos <= 100000 and not visited[next_pos]:
        visited[next_pos] = True
        distance[next_pos] = distance[current] + 1 # 각 위치에 이동한 거리 측정
        q.append(next_pos)

print(bfs(n))