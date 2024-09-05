# BOJ 10872 팩토리얼
n = int(input())

def factorial(n):
  if n == 1 or n == 0:
    return 1
  else: 
    return n * factorial(n-1)

print(factorial(n))

# BOJ 10870 피보나치 수 5

n = int(input())

def pibonacci(n) : 
  if n == 0:
    return 0
  elif  n == 1:
    return 1
  else :
    return pibonacci(n-1) + pibonacci(n-2)

print(pibonacci(n))
