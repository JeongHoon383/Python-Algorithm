# 백준 13116번

# 입력
# 첫째 줄에 테스트케이스 T
# 두번째 줄부터 정수 A와 B가 공백을 사이로 두고 주어짐

# 출력
# 꼭지점에 대응된 자연수 * 10

# 로직
# 반복문을 통해 두 노드의 가장 가까운 부모 노드를 찾는다.

import sys

n = int(sys.stdin.readline())

# 테스트 케이스만큼 반복
for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    while True:
        # 두 노드의 부모 노드가 같으면 반복을 멈춘다.
        if a == b:
            print(a * 10) # 부모 노드의 10배를 출력
            break
        if a > b:
            a //= 2
            # a가 더 클 경우 a의 부모 노드를 찾는다.
        else:
            b //= 2
            # b가 더 클 경우 b의 부모 노드를 찾는다.