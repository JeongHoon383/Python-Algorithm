t = int(input()) # 테스트 케이스의 수를 입력받음

for i in range(t): # 각 테스트 케이스에 대해 반복
  n = int(input()) # 현재 테스트 케이스에서 입력될 의상의 수 입력받음
  weardict = {} # 의상 종류별로 의상 이름을 저장할 딕셔너리

  for j in range(n): # n개의 의상 정보를 입력받음
    wear = list(input().split()) # 의상 이름과 의상 종류를 입력받아 리스트로 변환
    if wear[1] in weardict: # 의상 종류가 이미 딕셔너리에 있을 경우
      weardict[wear[1]].append(wear[0]) # 해당 종류에 의상 이름을 추가
    else: # 의상 종류가 딕셔너리에 없을 경우
      weardict[wear[1]] = [wear[0]] # 새로운 종류로 등록하고 해당 의상 이름을 추가

# 아래부터 이해 안됨
# 문제 
  # 1. 딕셔너리를 반복문 돌려주면 값이 나옴?
  # 2. 
  cnt = 1 # 의상 조합의 개수를 저장할 변수, 1로 초기화

  for k in weardict: # 의상 종류별로 반복, 
    cnt *= (len(weardict[k]) + 1) # 각 종류의 의상 개수에 "선택하지 않음" 옵션을 추가하여 곱셈

  print(cnt - 1) # 아무것도 입지 않는 경우를 제외하고 결과 출력