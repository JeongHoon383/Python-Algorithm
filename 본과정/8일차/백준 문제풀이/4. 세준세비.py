# 백준 1524번

# 입력
# 첫째 줄에 테스트 케이스의 개수 T
# 테스크 케이스 줄에는 첫째 줄에 N과 M이 들어오고 -> n : 세준이의 병사 수, m : 세비의 병사 수
# 둘째 줄 세준이의 병사들의 힘, 셋째 줄 세비의 병사들의 힘

# 출력
# 세준이가 이기면 S, 세비가 이기면 B, 둘 다 아닐경우 C
# 예외상황
# 1. 제일 약한 병사 죽음
# 2. 만약 제일 약한 병사 여러명이면 그 중 한명 임의로 선택되어 죽음
# 3. 하지만, 제일 약한 병사의 수가 같으면 세비의 병사가 죽음

# 로직
# 1. 테스트 케이스로 반복문
# 2. 첫째줄 n, m 으로 병사 수 받기
# 3. 세준이, 세빈이 병사를 담을 리스트 생성
# 4. 병사 오름차순으로 정렬

# 5. 반복문으로 병사 비교(전투) -> for문? while문? 
# 6. 힘이 약한 부대의 병사가 죽음
# 7. 만약 한 부대가 전멸하게 되면 이긴 부대의 병사가 한명 남을때까지 죽음
# 8. 한명이 남았을 때 병사가 있는 부대의 승리 

# 문제
# 각 테스트 케이스는 줄 바꿈으로 구분되어 있다. -> 이거 어떻게 표현?
# while 문의 조건을 생각하지 못함

t = int(input())
for i in range(t) :
    input()	# 각 테스트 케이스는 줄 바꿈으로 구분
    N, M = map(int, input().split())
    sj = sorted(list(map(int, input().split())), reverse=True)
    sb = sorted(list(map(int, input().split())), reverse=True)
    
    
    while sj and sb :
        if sj[-1] >= sb[-1] :	# 같거나 크면 세비의 병사 죽음, 내림차순으로 정렬해서 -1로 처리하는게 좋음 왜? 리스트는 스택의 역할로 LIFO 방식이기 때문
            sb.pop()
        else :
            sj.pop()
    
    if sj :
        print('S')
    elif sb :
        print('B')
    else :
        print('C')

# 내 풀이

# t = int(input())

# for _ in range(t):
#   n, m = int(input().split())
#   seJun = []
#   seBin = []
#   seJun.sort()
#   seBin.sort()
#   while True:

# 40740KB, 228ms