# 백준 18870번

# 입력
# 첫째 줄에 n이 주어짐
# 둘째 줄에는 공백 한 칸으로 구분된 X1, X2, ..., XN이 주어진다.

# 출력
# 첫째 줄에 X'1, X'2, ..., X'N을 공백 한 칸으로 구분해서 출력한다.

# 로직
# 문제 이해 못함

import sys

input = sys.stdin.readline

n = int(input()) # 좌표 개수
arr = list(map(int, input().split())) # 공백으로 주어진 좌표 받기

arr2 = sorted(list(set(arr))) 
# 중복을 제거한 좌표들을 정렬한 리스트 생성
# set()으로 중복을 제거하고, sorted()로 좌표를 오름차순으로 정렬

dic = {arr2[i] : i for i in range(len(arr2))}
# 각 좌표에 대해 압축된 값을 딕셔너리로 매핑, 아래와 같이 생성됨
      # dic = {
      #     -10: 0,  # arr2[0] = -10, 인덱스는 0
      #     -9: 1,   # arr2[1] = -9, 인덱스는 1
      #     2: 2,    # arr2[2] = 2, 인덱스는 2
      #     4: 3     # arr2[3] = 4, 인덱스는 3
      # }
# arr2의 좌표들을 0부터 시작하는 인덱스로 매핑하여 딕셔너리 생성

for i in arr:
    print(dic[i], end = ' ')

# 155280KB, 1812ms