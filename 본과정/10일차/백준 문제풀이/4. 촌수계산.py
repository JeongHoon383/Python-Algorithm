# 백준 2644번

# 입력
# 첫 줄에 전체 사람 수 N 입력
# 두 번째 줄에 촌수를 계산할 두 사람 A와 B 입력
# 세 번째 줄에 관계의 개수 M 입력
# 이후 M줄에 각각 서로 관계를 나타내는 두 사람의 번호가 공백으로 구분되어 입력

# 출력
# A와 B가 서로 촌수로 연결되어 있다면 그 촌수를 출력
# 만약 촌수 관계가 없으면 -1 출력

# 로직
# 1. DFS로 두 사람 간의 촌수를 탐색
# 2. 방문 여부를 체크하며 촌수를 계산
# 3. 만약 B에 도달하면 촌수를 기록하고, 끝까지 도달하지 못하면 -1 출력

N = int(input())  # 사람 수 N 입력
A, B = map(int, input().split())  # 촌수 계산할 두 사람 A, B 입력
M = int(input())  # 관계의 수 M 입력
graph = [[] for _ in range(N+1)]  # 관계를 저장할 그래프 (인접 리스트)
visited = [False] * (N+1)  # 방문 여부를 체크하기 위한 리스트
result = []  # 결과값을 저장할 리스트

# 관계 정보를 그래프에 저장 (무방향 그래프)
for _ in range(M):
    x, y = map(int, input().split())  
    graph[x].append(y)  # x와 y가 서로 관계가 있음
    graph[y].append(x)  # y와 x가 서로 관계가 있음

# DFS 탐색을 통해 촌수 계산
def dfs(v, num):
    num += 1  # 촌수를 증가
    visited[v] = True  # 현재 사람을 방문 처리

    if v == B:  # 만약 현재 방문한 사람이 B이면
        result.append(num)  # 촌수를 결과에 저장

    for i in graph[v]:  # 현재 사람과 연결된 모든 사람 탐색
        if not visited[i]:  # 아직 방문하지 않은 사람이라면
            dfs(i, num)  # 그 사람을 방문하여 촌수 계산

dfs(A, 0)  # A부터 시작하여 DFS 탐색 시작
if len(result) == 0:  # 만약 B에 도달하지 못했으면
    print(-1)  # -1 출력
else:
    print(result[0]-1)  # 촌수 출력 (처음 증가된 값을 제외해야 하므로 -1)

# 31120KB, 36ms
