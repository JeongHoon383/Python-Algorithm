## 입력
# input_var = input("숫자를 입력해주세요")
# print(input_var * 5) ## 문자열, int로 바꿔줘야됨

## 출력
# print("A", "B", sep=".", end='-') # ,는 공백으로 출력됨, sep="." 공백 대신 .이 출력됨
# print("B") # end 메서드를 사용하여 A.B-C 로 이어서 출력됨

## 길이
# v1 = "hello"
# v2 = [1, 2, 3]

# print(len(v1), len(v2))

# 개별 기능 적용
# def test(x):
#   return x * 2

# 이부분 다시 해보기
# v1 = [1, 5, 10]
# map_result = map(lambda x : x * 2, v1) # def 대신 lambda 사용
# v2 = list(map_result)
# print(v2)

# v1 = [1, 4, 10]
# print(min(v1), max(v1), sum(v1))

## 묶어주기
# list1 = [0, 1, 2, 3, 4]
# list2 = ['A', 'B', 'C', 'D', 'E']

# print(list(zip(list1, list2)))
# # 두 배열을 값의 위치에 맞게 묶어줌
# # 쌍의 수가 안맞으면 맞는 수 만큼만 묶어서 반환

# list4 = [10, 2, 7, 4, 5, 20, 58]
# print(list(reversed(list4))) # 거꾸로 된 값을 만듦

# for x in reversed(list4):
#   print(x) # 기존 list4를 역순으로 순회

# import sys
# data = sys.stdin.readline()
# print(data)

# input_str = input()
# input_nums = []

# nums = list(map(int, input_str.split()))

# 여러 줄 복수 값 입력

# 5
# 4 0 1 1
# 4 1 3 1
# 4 2 5 1
# 4 3 7 1

## 첫번째 N을 입력받아 int로 바꾸어 count 변수에 저장한다.
# count = int(input())

# list_of_list = []
# for _ in range(count-1):
#   # 입력을 받는다
#   parsed_list = list(map(int, input().split(" ")))
#   # input에 받은 요소들을 split으로 쪼개고 정수로 바꿔줌
#   list_of_list.append(parsed_list)
#   # list_of_list 에 추가, 만약 list_of_list가 없다면?
#   # parsed_list 가 반복문이 돌면서 초기화가 되기 때문에
#   # parsed_list 마지막 요소가 출력됨

# print(list_of_list)

# 여러개의 정수 입력 받기
num = list(map(int, input().split(" ")))
print(' '.join(map(str, sorted(num))))
# 2를 어떻게 출력하지?



