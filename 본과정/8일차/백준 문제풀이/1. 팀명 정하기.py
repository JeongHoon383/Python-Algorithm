# 백준 28114번

# 입력
# 해결한 문제의 개수, 입학 연도, 그리고 성씨
# 첫째 줄에 첫 번째 팀원이 해결한 문제 P, 입학 년도 Y, 성씨 S 가 공백으로 주어짐
# 둘째 줄, 셋 째줄 동일

# 출력
# 첫 번째 방법으로 출력(ex. 181920)
# 두 번째 방법으로 출력(OLA)

# 로직
# 값을 입력받고, 입학 연도를 담는 List, 해결한 문제의 개수, 성씨를 담는 List 만듬
# 각 List에 입력받은 값을 넣고 정렬
# 정렬된 값 이어 붙여주기

fList = []
sList = []

for i in range(3):
  P, Y, S = map(str, input().split())

  fList.append(int(Y) % 100)
  sList.append([int(P), S])

fList.sort() # [18, 19, 20]
sList.sort(reverse=True) # [[6000, 'OH'], [2000, 'LEE'], [600, 'AHN']]

fAns = ""
sAns = ""

for i in range(3):
  fAns += str(fList[i])
  sAns += (sList[i][1])[0]

print(fAns)
print(sAns)



