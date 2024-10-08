# 백준 2108번

# 입력
# 첫째 줄에 수의 개수 N이 주어짐 단, N은 홀수 - 5
# N개의 줄에는 정수들이 주어짐 - 1, 3, 8, -2, 2

# 출력
# 첫째 줄에는 산술평균을 출력한다. 소수점 이하 첫째 자리에서 반올림한 값을 출력 - N개의 수들의 합을 N으로 나눈 값 - (1 + 3 + 8 + -2 + 2) // 5 = 2
# 둘째 줄에는 중앙값을 출력 -  N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값 - [-2, 1, 2, 3, 8] = 2
# 셋째 줄에는 최빈값을 출력, 여러 개 있을 때에는 최빈값 중 두 번째로 작은 값을 출력 - N개의 수들 중 가장 많이 나타나는 값 - 개수가 제일 많은거 다만, 개수가 동일하가면 2번째로 작은거 출력 - 1
# 넷째 줄에는 범위를 출력 - N개의 수들 중 최댓값과 최솟값의 차이 - 8 - (-2) = 10

# 로직
# 1. 수의 개수, 정수 입력 받음
# 2. 입력받은 정수 배열에 저장, 배열 오름차순으로 정렬
# 3. 조건대로 출력

# 값, 쌍 만드는걸 잘 못함

import sys
input = sys.stdin.readline

n = int(input())
nums = []
count = {}

for _ in range(n):
    num = int(input())
    nums.append(num)

nums.sort()  # 오름차순 정렬

# 1. 산술 평균 (소수점 첫째 자리에서 반올림)
print(round(sum(nums) / n))

# 2. 중앙값
print(nums[n // 2])

# 3. 최빈값 구하기
for num in nums:
    if num in count:
        count[num] += 1
    else:
        count[num] = 1

# 최빈값 중 가장 큰 빈도수를 찾음
max_freq = max(count.values())

# 최빈값이 여러 개일 경우를 고려해서 빈도수가 같은 값들 리스트로 저장
modes = [key for key, value in count.items() if value == max_freq]

# 최빈값이 여러 개면 두 번째로 작은 값 출력, 하나면 그 값 출력
if len(modes) > 1:
    modes.sort()
    print(modes[1])  # 두 번째로 작은 값
else:
    print(modes[0])  # 하나뿐인 최빈값

# 4. 범위 (최댓값 - 최솟값)
print(max(nums) - min(nums))

# 52504KB, 496ms


# n = int(input())
# nums = []
# count = {}

# for _ in range(n):
#   num = int(input())
#   nums.append(num)

# nums.sort(reverse=False)

# print(sum(nums) // 5)
# print(nums[len(nums) // 2])
# # 가장 많이 나타나는 값을 어떻게 표현?
# # 배열의 요소 중 중복되는 값의 개수를 세야함
# # count에 key 값이 0일때 1을 추가해줌 - 헷갈림
# # value 값이 가장 큰 key 값을 출력 단, value 값이 가장 큰 key 값이 중복일 경우 그 key 값 중 두번째로 작은 값 출력 - 이부분 잘 모르겠음
# for i in nums : 
#   if count[i] == 0:
#     count[i] == 1
#   else :
#     count[i] += 1

# if count

# print(max(nums) - min(nums))

