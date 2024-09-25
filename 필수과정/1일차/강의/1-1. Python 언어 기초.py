x = 0.1 + 0.1 + 0.1 
y = 1 + 1 + 1 
print(x == 0.3) # False, 부동 소수점의 산술 연산(소수점, 실수 값) 중 적확도 문제
print(y == 3) # True, 정수값은 상관 없음

## 실수형 데이터의 오차
# round
print(round(x, 1) == 0.3) # True, 소수점 한자리까지만 출력

# isclose
from math import isclose # 파이썬의 표준 라이브러리인 math 모듈의 isclose 함수
print(isclose(x, 0.3)) # 값이 비슷(근접)하면 True 출력
# 가까운 정도는 어떻게 되지? 판단 기준 - 절대 오차와 상대 오차 활용

from decimal import Decimal
print(Decimal("0.1") +Decimal("0.1") +Decimal("0.1") == Decimal("0.3"))
# decimal을 활용하여 문자열 숫자를 넣어주면 좀 더 정확하게 판단 가능
# 문자열이 아닌 실수값 자체를 넘기게 되면 오차가 발생하여 False 반환

# 논리연산자 and, or, not
print(True or False) 

print(True and "String") # 우항의 값이 문자열이면 bool 타입이 아닌 우항의 값 출력
print(False or "String") # 둘중의 하나라도 문자열이면 문자열 출력

# 인덱싱, 슬라이싱
a = 'helao'

# print(a[0:4]) 세번째 콜론 - step, 기본값 1, step이 2면 1칸 띄고 다음걸 출력 2칸씩 출력
print(a[::-1]) # 거꾸로 출력, :step 