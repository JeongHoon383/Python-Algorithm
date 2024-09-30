# 문제 분석
# 그래프를 DFS로 탐색
# 그래프를 BFS로 탐색
# 단, 방문할 수 있는 정점이 여러개일 경우 번호가 작은것 먼저 방문
# 더 이상 방문할 수 없으면 종료

# 입력
N, M, V = map(int, input().split())

# 그래프 초기화
graph = [[0] * (N + 1) for _ in range(N + 1)]

# 간선 입력
for i in range(M):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1

# 방문 기록 처리
visited_bfs = [0] * (N + 1)
visited_dfs = [0] * (N + 1)  # 0은 미방문, 1은 방문

# dfs 함수 (반복문)
def dfs(V):
    stack = [V]
    while stack:
        node = stack.pop()
        if not visited_dfs[node] == 1:
            visited_dfs[node] = 1
            print(node, end=" ")
            for n in range(N, 0, -1):
                if graph[node][n] == 1 and visited_dfs[n] == 0:
                    stack.append(n)

# dfs 함수 (재귀)
def dfs_재귀(V):
    visited_dfs[V] = 1
    print(V, end=" ")
    for i in range(1, N + 1):
        if graph[V][i] == 1 and visited_dfs[i] == 0:
            dfs_재귀(i)

# bfs 함수
def bfs(V):
    queue = [V]
    visited_bfs[V] = 1
    while queue:
        node = queue.pop(0)
        print(node, end=" ")
        for i in range(1, N + 1):
            if graph[node][i] == 1 and visited_bfs[i] == 0:
                queue.append(i)
                visited_bfs[i] = 1


