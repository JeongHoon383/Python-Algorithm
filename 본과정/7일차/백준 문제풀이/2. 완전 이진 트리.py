# 백준 9934번 문제

# 입력
# 첫째 줄에 K가 주어진다.
# 둘째 줄에는 상근이가 방문한 빌딩의 번호가 들어간 순서대로 주어진다.

# 출력
# 총 K개의 줄에 걸쳐서 정답을 출력
# i번째 줄에는 레벨이 i인 빌딩의 번호를 출력

# 로직
# 문제 이해 안됨, 트리 이해 못함

def sol(start, end, level):
    # 주어진 구간 [start, end]에서 트리의 해당 레벨(level)에 맞는 노드를 추출하는 재귀 함수
    if start == end:
        ans[level].append(tree[start])
        return
    # 시작과 끝이 같으면 리프 노드이므로 해당 노드를 현재 레벨에 추가하고 종료
    center = (start + end) // 2
    # 중간 노드를 계산 (현재 구간의 중앙에 위치한 노드)
    ans[level].append(tree[center])
    # 현재 레벨에 중간 노드를 추가
    sol(start, center - 1, level + 1)
    # 왼쪽 하위 트리에 대해 재귀 호출 (구간: [start, center - 1])
    sol(center + 1, end, level + 1)
    # 오른쪽 하위 트리에 대해 재귀 호출 (구간: [center + 1, end])

Level = int(input())
# 트리의 레벨 (깊이)을 입력받음
tree = list(map(int, input().split()))
# 트리를 이루는 노드들의 배열을 입력받음
l = len(tree)
# 트리 배열의 길이
ans = [[] for _ in range(Level)]
# 각 레벨별로 노드를 저장할 리스트를 초기화 (레벨 개수만큼 빈 리스트 생성) - 왜 초기화?
sol(0, l - 1, 0)
# 재귀 함수 호출, 전체 트리 구간 [0, l-1]과 초기 레벨 0부터 시작
for a in ans:
    print(*a)
# 각 레벨에 저장된 노드들을 출력, *a -> 리스트의 요소를 공백 기준으로 출력

# 내풀이
# from sys import stdin
# n = int(stdin.readline())

# for _ in range(n):
#   num = list(map(int, stdin.readline().split()))
#   mid = num.pop(int(len(num) / 2))
#   print(mid)
