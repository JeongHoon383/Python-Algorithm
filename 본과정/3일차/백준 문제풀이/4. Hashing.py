# 문제 분석
# r의 값은 26보다 큰 소수인 31
#  M의 값은 1234567891
# 식을 통해 주어진 문자열의 해시 값을 계산하는 것

# 입력
# 첫 줄에는 문자열의 길이 L
# 둘째 줄에는 영문 소문자로만 이루어진 문자열

# 출력
# 문제에서 주어진 해시함수와 입력으로 주어진 문자열을 사용해 계산한 해시 값을 정수로 출력

n = int(input()) #제시할 문자열의 길이를 입력받는다.
str_ = list(input()) #문자열을 입력받아 리스트에 대입한다.
res = 0 # 출력할 변수 res를 선언한다.

for i in range(n): # 문자열의 길이만큼 반복한다.
    res += ((ord(str_[i]) - 96) * (31 ** i))
# 리스트 내 각각의 요소들은 아스키코드값으로 변경 후 96을 빼면 
# a는 1, b는 2의 값을 지니게 된다.
# 계수가 31이고 문자열의 순서에 따라 지수가 높아지므로 이를 고려하여 식을 짜면 위와 같다.

print(res % 1234567891)
# 해시 함수의 정의에서 유한한 범위의 출력을 가져야 한다고 했으므로 M(소수)을 나누어 출력한다.
# 해시 함수에서 충돌을 줄이기 위함

