# 문제 분석
# 1. 선끼리 교차하지 않음 : 연결선이 서로 엇갈리지 않고, 평행하게 배치되는 경우
# 2. 같은 글자는 다른 위치에 있음
# 3. 좋은 단어가 맞을 경우 count 추가

# 입력
# 1. 첫째 줄 단어의 수 N
# 2. A와 B로만 이루어진 단어가 한줄씩 입력

n = int(input())
ans = 0

for _ in range(n):
    stack = []
    _list = list(input())
    for i in _list:
        if not len(stack):
            stack.append(i)
        elif stack[-1] == i: # stack의 마지막 요소가 i와 같다면
            stack.pop(-1) # stack의 마지막 요소 제거
        else:
            stack.append(i)

    if not len(stack):
        ans += 1 

print(ans)