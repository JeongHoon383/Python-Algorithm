def fib(n) : 
    if n == 1 or n ==2:
      return 1
    else : 
      return fib(n-1) + fib(n-2)

def fibonacci(n):
    dp=[0]*(n+1) # 크기가 n+1인 리스트 dp를 생성하고, 모든 값을 0으로 초기화
    dp[1],dp[2]=1,1 # 피보나치 수열의 첫 번째와 두 번째 값은 각각 1로 설정
    cnt=0 # 반복문이 몇 번 실행되는지를 셀 변수 cnt2 초기화
    for i in range(3,n+1): # 3부터 n까지 반복
        cnt+=1 # 반복문이 한 번 실행될 때마다 cnt2 값을 1 증가
        dp[i]=dp[i-1]+dp[i-2] # 피보나치 수열의 점화식: dp[i] = dp[i-1] + dp[i-2
    return cnt # 계산이 몇 번 실행되었는지 반환

n=int(input())
print(fib(n),fibonacci(n))

# 시간 초과

# 동적계획법(DP)를 사용하여 피보나치 수 계산

def fib(n) : 
  f = [0] * (n+1) # [0] 을 제와한 n+1 만큼의 공간이 있는 배열 생성
  f[1] = 1
  f[2] = 1
  # 첫번째와, 두번째 피보나치 수를 구할 때는 각 1회 호출
  for i in range(3, n+1):
    f[i] = f[i-1] + f[i-2]
  # 첫번째, 두번째를 제외하고 3번째 부터 반복문 실행

  return f[n] # 재귀 함수가 호출되는 횟수는 피보나치 수와 일치

def fibonacci(n) : 
  return n-2 
# f(1), f(2)는 1로 사전 정의가 되어 있기 때문에, f(1)과 f(2)를 만들 때는 함수를 실행하지 않는다.
# 따라서 f(n)을 구할 때는 n-2번의 함수 실행이 되는 것을 알 수 있다.

n=int(input())
print(fib(n), fibonacci(n))
    