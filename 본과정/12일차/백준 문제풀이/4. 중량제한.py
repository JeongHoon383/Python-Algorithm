# 백준 1939번

# 입력
# 첫째 줄에 N, M
# M개의 줄에는 다리에 대한 정보를 나타내는 세 정수 A, B, C -> A번 섬과 B번 섬 사이에 중량제한이 C인 다리가 존재한다, 양방향
# 마지막 줄에는 공장이 위치해 있는 섬의 번호를 나타내는 서로 다른 두 정수가 주어진다

# 출력
# 한 번의 이동에서 옮길 수 있는 물품들의 중량의 최댓값 출력

# 로직

from sys import stdin
input = stdin.readline
n, m = map(int, input().split())
graph = [[] * n for _ in range(m)]
