# 1
nums = [1, 3, 2, 3, 4, 1, 2, 3, 4, 4]

# 딕셔너리를 사용하여 각 숫자의 빈도수를 구하세요.
# 출력 예시: {1: 2, 3: 3, 2: 2, 4: 3}

dict = {}

for num in nums:
  if num in dict:
    dict[num] += 1
  else : 
    dict[num] = 1

print(dict)

# 2
nums = [10, 15, 20, 25, 30]

# 리스트 내포를 사용하여 짝수만 추출하는 코드를 작성하세요.
# 출력 예시: [10, 20, 30]
even_nums = []

for num in nums:
  if num % 2 == 0:
    even_nums.append(num)

print(even_nums)

# 3
sentence = "파이썬은 자료구조와 알고리즘을 배우기에 아주 좋은 언어입니다"

# 딕셔너리를 사용하여 각 단어의 길이를 구하세요.
# 출력 예시: {'파이썬은': 3, '자료구조와': 4, '알고리즘을': 5, ...}

words = sentence.split()
wordsDict = {}

for word in words:
  if word not in wordsDict:
    wordsDict[word] = len(word)

print(wordsDict)

# 4
nums = [7, 5, 10, 3, 10, 6]

# 최댓값과 그 값의 인덱스를 구하세요.
# 출력 예시: 최댓값: 10, 인덱스: [2, 4]

max_num = max(nums)
max_idx = []

for i in range(len(nums)):
  if nums[i] == max_num:
    max_idx.append(i)

print(f"최댓값: {max_num}, 인덱스: {max_idx}")

# 5
nums = [1, 3, 3, 2, 2, 4, 1, 2, 4, 4]

# 딕셔너리를 사용하여 최빈값을 구하세요.
# 출력 예시: 3

dict = {}

for num in nums:
  if num in dict:
    dict[num] += 1
  else:
    dict[num] = 1

max_count = max(dict.values())

modes = [key for key, value in dict.items() if value == max_count]

if len(modes) > 1:
  modes.sort() # 오름차순 정렬
  print(modes[1]) # 두번째로 작은 수 출력
else:
  print(modes[0]) 



