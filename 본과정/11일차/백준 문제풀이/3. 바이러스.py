# 백준 2606번

# 입력
# 첫째 줄에는 컴퓨터의 수 - 노드
# 둘째 줄에는 네트워크 상에서 직접 연결되어 있는 컴퓨터 쌍의 수가 주어진다. - 간선
# 수만큼 한 줄에 한 쌍씩 네트워크 상에서 직접 연결되어 있는 컴퓨터의 번호 쌍 - 노드 관계

# 출력
# 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수
# 1번과 연결되어 있다는 것을 알아야됨 - ???
# 1번에서 2번을 갔을 때 2번도 전염 
# 전염되는걸 어떻게 표현?

# 로직
# 노드, 간선 입력 받음
# 그래프 생성
# 방문 횟수 수정

# 문제
# dfs, bfs 부분 작성 못함 
# 탐색 전 그래프 세팅까지는 현재 가능

# from collections import deque
from sys import stdin
input = stdin.readline
n = int(input()) # 노드 7
s = int(input()) # 간선 6

graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)

for _ in range(s):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)
  # graph = [[], [2, 5], [1, 3, 5], [2], [7], [1, 2, 6], [5], [4]]
# DFS 방식
def dfs(start):
    visited[start]=1
    for nx in graph[start]:
        if visited[nx]==0:
            dfs(nx)
dfs(1)
print(sum(visited)-1)
# 31120KB 32ms

# BFS 방식
# visited[1]=1 # 1번 컴퓨터부터 시작이니 방문 표시
# Q=deque([1])
# while Q:
#     c=Q.popleft()
#     for nx in graph[c]:
#         if visited[nx]==0:
#             Q.append(nx)
#             visited[nx]=1
# print(sum(visited)-1)
# 34052KB, 48ms