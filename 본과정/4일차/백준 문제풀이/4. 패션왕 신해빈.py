# 문제 분석
# 여러옷이 있는데 한 번 입으면 다시 못입음
# 하나라도 입은 상태로 며칠동안 밖에 돌아다닐 수 있을까? 

# 입력
# 첫째 줄에 테스트 케이스
# 테스트 케이스의 첫째 줄에는 해빈이가 가진 의상의 수 n
# n개에는 해빈이가 가진 의상의 이름과 의상의 종류가 공백으로 구분

# 출력
# 각 테스트 케이스에 대해 해빈이가 알몸이 아닌 상태로 의상을 입을 수 있는 경우를 출력

# 문제를 겪은 부분
# 공백 기준으로 띄어쓰기가 있는 단어 딕셔너리에 어떻게 넣지?
# 중복이 되지 않게 값을 저장해줌 - 어떻게?

t = int(input())  # 테스트 케이스의 수를 입력받음

for i in range(t):  # 각 테스트 케이스에 대해 반복
    n = int(input())  # 현재 테스트 케이스에서 입력될 의상의 수를 입력받음
    weardict = {}  # 의상 종류별로 의상 이름을 저장할 딕셔너리

    for j in range(n):  # n개의 의상 정보를 입력받음
        wear = list(input().split())  # 의상 이름과 의상 종류를 입력받아 리스트로 변환
        if wear[1] in weardict:  # 의상 종류가 이미 딕셔너리에 있을 경우
            weardict[wear[1]].append(wear[0])  # 해당 종류에 의상 이름을 추가
        else:  # 의상 종류가 딕셔너리에 없을 경우
            weardict[wear[1]] = [wear[0]]  # 새로운 종류로 등록하고 해당 의상 이름을 추가

    cnt = 1  # 의상 조합의 개수를 저장할 변수, 1로 초기화 (곱셈을 위해)

    for k in weardict:  # 의상 종류별로 반복, k에는 키 값이 담김
        cnt *= (len(weardict[k]) + 1)  # 각 종류의 의상 개수에 '선택하지 않음' 옵션을 추가하여 곱셈

    print(cnt - 1)  # 아무것도 입지 않는 경우를 제외하고 결과 출력
