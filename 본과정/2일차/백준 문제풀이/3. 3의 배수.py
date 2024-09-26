# 문제 분석
# 문제를 바라보는 시각을 다르게 한다. 
# 문제에 대한 답을 다시 문제로 변환한다. 
# 3의 배수는 한자리 수 밖에 없다고 가정한다. 
# 문제 변환의 과정을 여러 번 거치다 보면 Y가 한 자리 수가 되는 순간이 있다. 
# 큰 수 X가 주어졌을 때, 몇 번 거쳐야 Y가 한 자리 수가 되는가
# X가 3의 배수인지 아닌지를 알 수 있게 될지를 구하는 프로그램을 작성

# 로직 (굳이 y, z, w 변수를 사용할 필요 없음, while 문 사용해서 최종값 초기화)
# X 가 3의 배수인가? 를 먼저 확인하기 위해 X의 각 자리의 수를 더해준다. 그리고 그걸 Y라고 부른다.
# 그렇다면 Y는 3의 배수인가?를 확인하기 위해 Y의 값 또한 한자리가 아니므로 각 자리의 수를 더해준다. 그리고 그걸 Z라고 부른다.
# Z는 3의 배수인가? Z 역시 한자리 수가 아니므로 각 자리의 수를 더해준다. 그리고 그걸 W라고 부른다.
# W는 3의 배수인가? W는 한자리 이므로 3의 배수인지 확인한다.
# 3의 배수가 맞다면 YES, 아니라면 NO를 출력

# 입력
# 첫째 줄에 큰 자연수 X가 주어진다.

# 출력
# 첫째 줄에 문제 변환의 과정을 몇 번 거쳤는지를 출력
# 둘째 줄에는 주어진 수가 3의 배수이면 YES, 아니면 NO를 출력

# 알게 된 내용
# input으로 입력받은 값은 문자열로 반환됨. 숫자도 마찬가지
# while문을 아예 생각 못함. 반복되는 계산은 while 문 사용할 것

n = input()
c=0
while len(n)>=2:
    t = 0 # 각 자리의 수를 합한 값
    for i in range(len(n)):
        t+=int(n[i]) # 각 자리의 수 합 구해주기
    n=str(t) # n을 다시 문자열로 변환 why? while문 실행시 n이 int형이면 len 함수에서 에러
    c+=1 # 작업을 실행 했을 때 실행한 횟수 증가
print(c)
if int(n)%3==0: # 3의 배수인지 확인
    print("YES")
else:   
    print('NO')

# 내 풀이 : 로직은 맞으나 while 문을 생각 못함
# x = input()
# y = 0
# z = 0
# w = 0
# answer = 0

# for i in range(len(x)):
#   y += int(x[i])
# else : answer += 1

# for i in range(len(str(y))):
#   z += int(str(y)[i])
# else : answer += 1

# for i in range(len(str(z))):
#   w += int(str(z)[i])
# else : answer += 1

# if(w % 3 == 0):
#   print(answer)
#   print("YES")
# else:
#   print(answer)
#   print("NO")
