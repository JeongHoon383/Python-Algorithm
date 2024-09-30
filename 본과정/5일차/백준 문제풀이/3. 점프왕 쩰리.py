# 문제 분석
# 1. 가로, 세로 칸 수가 같은 정사각형의 구역 내부에서 움직일 수 있음. 쩰리가 외부로 나가면 패배
# 2. 출발점은 0, 0
# 3. 이동 방향은 오른쪽과 아래
# 4. 가장 오른쪽, 가장 아래 도착시 승리
# 5. 이동할 수 있는 칸의 수 지정

# 입력
# 첫 번째 줄에는 게임 구역의 크기 N
# 두 번째 줄부터 마지막 줄까지 게임판의 구역(맵)
# 게임판의 승리 지점(오른쪽 맨 아래 칸)에는 -1이 쓰여있고, 나머지 칸에는 0 이상 100 이하의 정수가 쓰여있다.

# DFS

import sys
input=sys.stdin.readline

def dfs(x,y) :
    #영역을 벗어났거나 이미 방문을 했다면 return
    if x<=-1 or x>=N or y<=-1 or y>=N or visit[x][y]==1:
        return
    
    #방문한 곳의 이동 칸 수가 -1이라면 방문처리를 해주고 return 한다. 
    if graph[x][y] == -1 :
        visit[x][y] = 1
        return

    #방문했다고 표시해준다.
    visit[x][y]=1

    #상,하,좌,우를 요소 수만큼 점프하여 방문한다.
    dfs(x+graph[x][y],y)
    dfs(x,y+graph[x][y])
#게임 구역의 크기 N을 입력받는다.
N=int(input())

#게임판의 구역을 입력받는다. 2차원 리스트
graph=[list(map(int,input().split())) for _ in range(N)]

#방문여부를 저장할 visit 2차원 리스트를 만든다.
visit=[[0]*N for _ in range(N)]

#출발은 0,0에서 하므로 dfs(0,0)을 호출한다.
dfs(0,0)

#결과 출력
if visit[-1][-1] == 1 :
    print('HaruHaru')
else :
    print('Hing')



# BFS

from collections import deque
N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

# 방문 유무 확인
visited = [[False]*3 for _ in range(N)]

# 오른쪽만 가능
dx = [1,0]

# 아래만 가능
dy = [0,1]

def bfs(x, y):
  
  q = deque()
  q.append([x,y])
  

  while q:
    x, y = q.popleft()
    # 쪨리가 현재 밟고 있는 칸의 숫자를 인출해준다.
    step = graph[x][y]

    # 끝점이 -1이므로 -1로 도달하면 성공!
    if graph[x][y] == -1:
      return True
    for move in range(2):
      # 쩰리가 현재 밟고 있는 숫자를 인출하고 이동수에 곱해서 이동해준다. 
      nx = x+dx[move]*step
      ny = y+dy[move]*step
      
      # 주어진 범위를 벗어나는 경우 무시
      # x, y의 범위가 0,0보다 작아지거나, 주어진 matrix의 크기를 초과하는 경우
      if nx < 0 or nx >= N or ny < 0 or ny >= N:
        continue

      # 방문하지 않았을경우만
      if not visited[nx][ny]:
        # 방문으로 수정해준다.
        visited[nx][ny] = True
        # 아직 우리가 찾는 조건(graph[x][y] == -1)이 아니므로 q에 담아주고 다시 반복해준다.
        q.append([nx, ny])  
        
if bfs(0,0):
    print('HaruHaru')
else:
    print('Hing')