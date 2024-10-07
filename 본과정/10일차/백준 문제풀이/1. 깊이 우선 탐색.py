# 백준 24479번

# 입력
# 첫째 줄에 정점의 수 n, 간선의 수 m, 시작 정점 r 주어짐
# 다음 m개 줄에 정점 u, v

# 출력
# 첫째 줄부터 N개의 줄에 정수를 한 개씩 출력한다. i번째 줄에는 정점 i의 방문 순서를 출력

# 로직
# 1. 정점 수 n, 간선 수 m, 시작 정점 r 입력 받음
# 2. 간선 수로 반복문, dfs 함수 생성
# 3. 

# 스택 방식 - 구글링

import sys
input = sys.stdin.readline

N, M, R = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, len(graph)):
    graph[i].sort(reverse=True)

def DFS(start):
    stack = [start]  
    visited = [-1] * (N + 1)  
    result = [0] * (N + 1)  
    cnt = 1  

    
    while stack:
        cnt_node = stack.pop()  
        if visited[cnt_node] == 1:  
            continue  
        visited[cnt_node] = 1 
        result[cnt_node] = cnt  
        cnt += 1  
        
        for adj_node in graph[cnt_node]:
            if visited[adj_node] == -1:
                stack.append(adj_node)
    
    return result

result = DFS(R)

print(*result[1:], sep="\n")

# 61408KB, 544ms


# 내풀이
# n, m, r = map(int, input().split())

# for _ in range(m):
#   visited = [False for _ in range()]
#   dfs(r)