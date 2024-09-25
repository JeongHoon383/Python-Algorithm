num = int(input())
stars = [[' ' for _ in range(4 * num - 3)] for _ in range(4 * num - 3)] # 전체 별 배열 초기화 (크기는 4 * num - 3)
# 별을 그리는 함수
def fill_star(n, x, y):
    if n == 1:
        stars[y][x] = '*'  # 가장 작은 크기의 별은 중앙에 하나의 '*'만 그립니다.
        return
    length = 4 * n - 3  # 현재 그려야 할 사각형의 한 변의 길이
    # 위쪽 가로 줄
    for i in range(length):
        stars[y][x + i] = '*'  # 상단 가로줄
        stars[y + length - 1][x + i] = '*'  # 하단 가로줄
    # 왼쪽 세로 줄
    for i in range(length):
        stars[y + i][x] = '*'  # 왼쪽 세로줄
        stars[y + i][x + length - 1] = '*'  # 오른쪽 세로줄
    # 재귀적으로 내부 작은 사각형을 그리기
    fill_star(n - 1, x + 2, y + 2)
# 함수 호출
fill_star(num, 0, 0)
# 결과 출력
for s in stars:
    print(''.join(s))