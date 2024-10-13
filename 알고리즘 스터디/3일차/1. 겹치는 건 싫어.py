# 백준 20922번

# 입력
# 첫째줄에 N과 K
# 둘째줄에 N개의 수열 띄어쓰기 기준으로 나열

# 출력
# 조건을 만족하는 최장 연속 부분 수열의 길이를 출력

# 로직
# 1. 투 포인터 사용 : left와 right 두 포인터를 이용하여 배열의 부분 수열 탐색
# 2. 등장 횟수 기록 : counter 배열을 사용하여 각 숫자가 현재 부분 수열 내에서 몇 번 등장했는지 기록
# 3. 조건 확인 : right 포인터가 가리키는 숫자가 K번 미만으로 등장했을 경우, right를 확장하고, 그렇지 않으면 left를 움직여 범위를 좁힘
# 4. 결과 갱신 right - left로 현재 부분 수열의 길이를 계산하고, 가장 긴 부분 수열의 길이를 answer에 갱신

# N: 배열의 길이, K: 숫자가 최대 등장할 수 있는 횟수
N, K = map(int, input().split())

# numbers: 주어진 숫자 배열
numbers = list(map(int, input().split()))

# 투 포인터로 사용할 left와 right를 0으로 초기화
left, right = 0, 0

# counter: 각 숫자가 몇 번 등장했는지를 저장하는 리스트, 숫자의 최대값 + 1 크기로 생성
counter = [0] * (max(numbers) + 1)

# answer: 가장 긴 부분 수열의 길이를 저장할 변수
answer = 0

# right 포인터가 배열의 끝에 도달할 때까지 반복
while right < N:
    
    # 현재 right 포인터가 가리키는 숫자가 K번 미만으로 등장했을 경우
    if counter[numbers[right]] < K:
        # 해당 숫자의 등장 횟수를 증가시키고
        counter[numbers[right]] += 1
        # right 포인터를 오른쪽으로 이동시켜 부분 수열을 확장
        right += 1
    else:
        # 현재 숫자가 K번 이상 등장했을 경우
        # left 포인터를 오른쪽으로 이동시키면서, left가 가리키는 숫자의 등장 횟수를 감소시킴
        counter[numbers[left]] -= 1
        left += 1

    # 현재 부분 수열의 길이 (right - left)를 계산하고 최대값을 answer에 저장
    answer = max(answer, right - left)

# 가장 긴 부분 수열의 길이를 출력
print(answer)

