import sys
input = sys.stdin.readline

dict = {} # 과일을 저장 할 dictionary 생성
for _ in range(int(input())):
    s, n = input().split() # 과일이름, 개수 입력 받음
    dict[s] = dict.get(s, 0) + int(n) # 딕셔너리에 해당 과일 이름이 있으면 과일 개수 합산, 없으면 0 반환

for n in dict: # 딕셔너리에 값 판별
    if dict[n] == 5:
        print('YES')
        exit()
print('NO')

