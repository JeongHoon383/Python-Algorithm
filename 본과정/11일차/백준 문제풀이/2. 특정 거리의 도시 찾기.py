# 백준 18352번

# 입력
# 첫째 줄에 도시의 개수 N - 정점, 도로의 개수 M - 간선, 거리 정보 K - 최단 거리, 출발 도시의 번호 X - 현재 위치가 주어진다. -> 4 4 2 1
# 둘째 줄부터 M개의 줄에 걸쳐서 두 개의 자연수 A, B가 공백을 기준으로 구분되어 주어진다.

# 출력
# 최단 거리가 K인 모든 도시의 번호를 한 줄에 하나씩 오름차순으로 출력
# 최단 거리가 K인 도시가 하나도 존재하지 않으면 -1을 출력

# 로직
# 도시 개수(노드) 입력받고 그래프 생성 시작점 1부터
# 

# 문제
# 스택 -> 데이터 넣고, 빼는 과정이 머리속에 잘 안그려짐 스택부분이 보완 필요할듯

from collections import deque
import sys
input = sys.stdin.readline

# 입력 받기
# n: 도시의 개수, m: 도로의 개수, k: 거리 정보, x: 출발 도시 번호
n, m, k, x = map(int, input().split())

# 각 도시를 연결하는 그래프 (도시 번호는 1부터 시작하므로 n+1)
graph = [[] for _ in range(n+1)]

# 각 도시까지의 최단 거리를 기록하는 리스트
distance = [0] * (n+1)

# 방문 여부를 기록하는 리스트
visited = [False] * (n+1)

# 도로 정보 입력 (a에서 b로 가는 도로가 존재함)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

# BFS(너비 우선 탐색) 함수 정의
def bfs(start): # 초기 start = 1
    # k 거리 만큼 떨어진 도시들을 저장할 리스트
    answer = []
    
    # BFS를 위한 큐 선언, 시작 도시를 큐에 넣음
    q = deque([start])
    
    # 시작 도시는 방문 처리하고, 거리는 0으로 설정
    visited[start] = True
    distance[start] = 0
    
    # 큐가 빌 때까지 탐색 진행
    while q:
        now = q.popleft()  # 큐에서 현재 도시를 꺼냄
        
        # 현재 도시와 연결된 다른 도시들을 탐색
        for i in graph[now]:
            if not visited[i]:  # 아직 방문하지 않은 도시만 탐색
                visited[i] = True  # 해당 도시 방문 처리
                q.append(i)  # 큐에 추가하여 다음에 탐색할 도시로 설정
                distance[i] = distance[now] + 1  # 현재 도시까지의 거리에서 1 증가
                
                # 만약 목표 거리 k만큼 떨어져 있으면 answer 리스트에 추가
                if distance[i] == k:
                    answer.append(i)
    
    # k 거리만큼 떨어진 도시가 없다면 -1 출력
    if len(answer) == 0:
        print(-1)
    else:
        # k 거리만큼 떨어진 도시를 오름차순으로 정렬 후 출력
        answer.sort()
        for i in answer:
            print(i, end='\n')

# 출발 도시 x에서 BFS 실행
bfs(x)

# 100984KB, 1664ms


# 내풀이
# from sys import stdin

# N, M, K, X = map(int, stdin.readline().split())
# graph = [[] for _ in range(N + 1)]

# for i in range(1, M + 1):
#   a, b = map(int, stdin.readline().split())
#   graph[i].append(a) # 그래프 세팅부터 막힘, 단방향 간선을 어떻게 표현?

# # graph.sort(reverse=True) # 내림차순으로 정렬 왜? 오름차순으로 출력해야됨

# print(graph)