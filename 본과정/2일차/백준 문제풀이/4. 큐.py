# 문제 분석
# 정수를 저장하는 큐를 구현
# 입력으로 주어지는 명령을 처리하는 프로그램을 작성

# 로직
# 1. 정수를 저장하는 큐 구현
# 2. 명령에 맞춰서 조건식 작성

# 입력
# 1. 첫째 줄에 주어지는 명령의 수 N이 주어진다
# 2. 둘째 줄부터 명령이 주어진다. 

# 출력
# 1. 명령에 맞춰서 출력

from sys import stdin

N = int(stdin.readline())
Que = []
for i in range(N) :
    A = stdin.readline().split()

    if A[0] == 'push' : Que.append(A[1])

    elif A[0] == 'pop' : 
        if Que : print(Que.pop(0))
        else : print(-1)

    elif A[0] == 'size' : print(len(Que))

    elif A[0] == 'empty' :
        if len(Que) == 0 : print(1)
        else : print(0)
            
    elif A[0] == 'front' :
        if len(Que) == 0 : print(-1)
        else : print(Que[0])
    
    elif A[0] == 'back' :
        if len(Que) == 0 : print(-1)
        else : print(Que[-1])